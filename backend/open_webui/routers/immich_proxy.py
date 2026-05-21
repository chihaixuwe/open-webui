from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse
import aiohttp
import os
from datetime import timedelta
from typing import List

from open_webui.utils.auth import get_current_user, create_token

router = APIRouter()

IMMICH_BASE = os.environ.get('IMMICH_BASE_URL', 'http://immich-server:3001')

# Paths allowed to be proxied for security. Adjust as needed.
ALLOWED_PREFIXES = [
    '/api/albums',
    '/api/assets',
    '/api/uploads',
    '/api/thumbnail',
    '/api/search',
]


def make_immich_token(user):
    payload = {'id': user.id, 'email': getattr(user, 'email', ''), 'role': getattr(user, 'role', 'user')}
    return create_token(payload, expires_delta=timedelta(minutes=60))


def is_allowed_path(path: str) -> bool:
    p = '/' + path.lstrip('/')
    return any(p.startswith(pref) for pref in ALLOWED_PREFIXES)


async def forward_request(request: Request, url: str, headers: dict, data=None, params=None):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.request(request.method, url, headers=headers, data=data, params=params) as resp:
                content = await resp.read()
                resp_headers = {k: v for k, v in resp.headers.items()}
                return StreamingResponse(content=content, status_code=resp.status, headers=resp_headers)
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))


@router.api_route('/api/immich/{path:path}', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
async def immich_proxy(path: str, request: Request, user=Depends(get_current_user)):
    """Proxy to Immich with JWT signed by WebUI. Only allowed prefixes are forwarded."""

    if not is_allowed_path('/' + path):
        raise HTTPException(status_code=403, detail='Path not allowed')

    url = f"{IMMICH_BASE}/{path}"
    headers = {k: v for k, v in request.headers.items() if k.lower() != 'host'}
    token = make_immich_token(user)
    headers['Authorization'] = f'Bearer {token}'

    # If multipart/form-data upload, forward stream preserving form fields/files
    content_type = request.headers.get('content-type', '')
    if content_type.startswith('multipart/form-data'):
        # Read form data via starlette's request.form()
        form = await request.form()
        data = {}
        files = []
        for k, v in form.multi_items():
            # UploadFile or str
            if hasattr(v, 'filename'):
                files.append((k, (v.filename, v.file, v.content_type)))
            else:
                data.setdefault(k, []).append(v)

        # aiohttp requires files to be in a specific format; build multipart data
        from aiohttp import FormData

        fd = FormData()
        for k, vals in data.items():
            for item in vals:
                fd.add_field(k, str(item))
        for k, (filename, fileobj, ctype) in files:
            # fileobj is a SpooledTemporaryFile; rewind
            try:
                fileobj.seek(0)
            except Exception:
                pass
            fd.add_field(k, fileobj, filename=filename, content_type=ctype)

        return await forward_request(request, url, headers, data=fd, params=dict(request.query_params))

    # For non-multipart, forward raw body
    body = await request.body()
    return await forward_request(request, url, headers, data=body, params=dict(request.query_params))
