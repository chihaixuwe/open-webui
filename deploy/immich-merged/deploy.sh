#!/usr/bin/env bash
set -euo pipefail

# 简易一键部署脚本（在 deploy/immich-merged 目录下运行）
# 说明: 脚本会创建宿主目录、拷贝 .env（如缺失）、并用 sudo 启动 docker compose。

cwd=$(cd "$(dirname "$0")" && pwd)
cd "$cwd"

echo "当前目录: $cwd"

# 确保 .env 存在
if [ ! -f .env ]; then
  if [ -f .env.example ]; then
    cp .env.example .env
    echo "已从 .env.example 复制 .env，请检查并按需修改。"
  else
    echo ".env.example 不存在，请先准备好环境变量文件。"
    exit 1
  fi
fi

# 创建宿主卷目录并设置权限
echo "创建宿主卷目录 /srv/immich/uploads 和 /srv/immich/pgdata（需要 sudo）..."
sudo mkdir -p /srv/immich/uploads /srv/immich/pgdata
sudo chown "$USER":"$USER" /srv/immich/uploads /srv/immich/pgdata

# 启动堆栈
echo "开始构建并启动容器（需要 sudo）..."
sudo docker compose -f docker-compose.yml up -d --build

# 显示状态和简短日志
sudo docker compose -f docker-compose.yml ps
sudo docker compose -f docker-compose.yml logs --tail 100

echo "部署脚本执行完毕。若容器未启动或报错，请把最后的日志复制给我。"
