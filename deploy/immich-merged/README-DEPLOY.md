快速部署说明

1) 前提
- 主机安装 Docker 与 Docker Compose（或 Docker Compose V2）。
- 有 sudo 权限（脚本会要求）。

2) 一键部署
在仓库中运行：

```bash
cd /www/wwwroot/deepay.srl/deepay-ai-platform/deploy/immich-merged
# 可先编辑 .env（如果需要）
chmod +x deploy.sh
./deploy.sh
```

脚本会：
- 如缺失则从 `.env.example` 复制 `.env`（请检查并修改为你的密码/密钥）。
- 在宿主机创建 `/srv/immich/uploads` 和 `/srv/immich/pgdata` 并将归属改为当前用户（需要 sudo）。
- 使用 `sudo docker compose -f docker-compose.yml up -d --build` 启动服务。

3) 常见问题
- 如果看见 `permission denied`，请确认当前用户在 `docker` 组，或以 `sudo` 执行脚本。
- 若需要我生成不同的 secret 值或调整端口，请告知要替换的变量。

4) 我可以帮你做的事
- 生成并提交一个定制的 `.env`（含真实值）
- 将 compose 转为 Kubernetes manifests
- 把 webui 改为不依赖宿主卷的测试模式（快速 smoke test）

把你要我自动替换的 `.env` 值（例如数据库密码、域名、是否在 80 上运行等）发给我，我可以直接把 `.env` 写好。