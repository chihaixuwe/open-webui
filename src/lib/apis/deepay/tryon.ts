import { WEBUI_BASE_URL } from '$lib/constants';

export const tryonCommand = async (token: string, image: File, command: string) => {
	let error = null;

	const formData = new FormData();
	formData.append('image', image);
	formData.append('command', command);

	const res = await fetch(`${WEBUI_BASE_URL}/api/ai/tryon/command`, {
		method: 'POST',
		headers: {
			authorization: `Bearer ${token}`
		},
		body: formData
	})
		.then(async (res) => {
			if (!res.ok) throw await res.json();
			return res.json();
		})
		.catch((err) => {
			error = err;
			console.error(err);
			return null;
		});

	if (error) {
		throw error;
	}

	return res;
};

export const tryonSession = async (token: string) => {
	let error = null;

	const res = await fetch(`${WEBUI_BASE_URL}/api/ai/tryon/session`, {
		method: 'GET',
		headers: {
			Accept: 'application/json',
			'Content-Type': 'application/json',
			authorization: `Bearer ${token}`
		}
	})
		.then(async (res) => {
			if (!res.ok) throw await res.json();
			return res.json();
		})
		.catch((err) => {
			error = err;
			console.error(err);
			return null;
		});

	if (error) {
		throw error;
	}

	return res;
};

export const tryonAvatar = async (token: string, avatar: string) => {
	let error = null;

	const res = await fetch(`${WEBUI_BASE_URL}/api/ai/tryon/avatar`, {
		method: 'POST',
		headers: {
			Accept: 'application/json',
			'Content-Type': 'application/json',
			authorization: `Bearer ${token}`
		},
		body: JSON.stringify({ avatar })
	})
		.then(async (res) => {
			if (!res.ok) throw await res.json();
			return res.json();
		})
		.catch((err) => {
			error = err;
			console.error(err);
			return null;
		});

	if (error) {
		throw error;
	}

	return res;
};
