# Immich 合并部署示例（方案三）

快速说明：本目录提供一个最小示例，以演示如何将 Immich 作为 Headless Service 与你自己的 WebUI 共享数据库与存储。

步骤概览：

1. 复制 `.env.example` 为 `.env` 并填写变量。
2. 在宿主机创建共享目录：

```bash
sudo mkdir -p /srv/immich/uploads /srv/immich/pgdata
sudo chown -R 1000:1000 /srv/immich/uploads /srv/immich/pgdata
```

3. 确保你把 `WEBUI_SECRET_KEY` 在你的 WebUI 与 Immich 中保持一致（Immich 的 `JWT_SECRET` 应设置为相同值）。
4. 启动：

```bash
cd deploy/immich-merged
docker compose up -d
```

关键注意事项：
- 请锁定 Immich 镜像版本（不要使用 `latest`）。示例使用 `ghcr.io/immich-app/immich-server:v1.100.0`。
- 确保运行容器的 UID/GID 与宿主目录权限一致，避免文件读写问题。
- 不要让 WebUI 修改 Immich 的 ML 容器或其数据库模型，ML 功能应由 Immich 自己负责。
-- 在生产环境使用外部密钥管理（KMS）或更安全的 secret 管理方案保存 `WEBUI_SECRET_KEY`（并把同一密钥注入到 Immich 的 `JWT_SECRET`）。

接下来的可选工作：
- 将 `webui` 服务替换为你的 WebUI 镜像或 `build:` 指令，并 pin 版本。
- 添加 Nginx 反向代理和 TLS 配置以实现静态资源直链和安全访问。
