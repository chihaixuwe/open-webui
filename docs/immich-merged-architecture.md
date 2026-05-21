# 架构同源（方案三）——终极落地指南（含 Lava 中枢）

本指南将方案三扩展为企业级融合架构：Lava 作为系统中枢（Root），Immich 作为无头媒体服务，WebUI 作为前端呈现层。

概念比喻：Lava 是大脑/心脏，Immich 是视觉神经，WebUI 是脸面。

---

## 核心原则（快速回顾）

- 共用数据库：统一的 PostgreSQL，Lava 为主库，Immich 的用户表不再对外使用。
- 共用存储：宿主机卷映射，WebUI、Lava 与 Immich 使用同一物理路径存储媒体。
- 统一鉴权：Lava 签发 JWT，Immich 与 WebUI 信任同一 `LAVA_JWT_SECRET`。
- BFF/网关：所有外部流量从 Lava 或 API 网关进入，Immich 只接收来自可信后端的请求。

---

## 架构要点

1) Lava 为唯一中枢

- 负责：用户、店铺、订单、RBAC、支付网关、签发 JWT、业务规则。
- 代理：对 Immich 的所有写入或读取请求由 Lava 做权限校验与代理（或通过受控服务账号调用）。

2) Immich 去用户化

- 禁用注册/密码登录（`DISABLE_SIGNUP=true`、`DISABLE_PASSWORD_LOGIN=true`）。
- Immich 只做媒体入库、缩略图生成、AI 识别；用户语义由 Lava 提供。

3) WebUI 只做展示

- 前端调用 Lava/OpenAPI，Lava 决定是否代理或直接返回包含 Immich 资源 URL 的数据给前端。

---

## 数据设计建议

- 将业务表（如 `products`、`orders`、`shops`、`users`）放在 Lava 库。
- 在 Lava 中维护 `product_media` 表：记录 `product_id` ↔ `immich_asset_id` 的映射。
- Immich 的 media 表继续存在，用于内部索引与检索，但业务解释权在 Lava。

---

## 典型业务流程（上传商品图）

1. 用户在 WebUI 提交图片给 Lava（经前端）
2. Lava 校验权限 -> 调用 Immich 上传 API（携带 Lava 签发的 JWT 或服务账户）
3. Immich 返回 Asset ID -> Lava 将 Asset ID 写入 `product_media`（关联 product_id）
4. 前端展示时，WebUI 请求 Lava，Lava 返回包含 Immich 缩略图 URL 的业务数据

---

## 部署拓扑（建议）

[ Browser ] -> [ Nginx / API Gateway ] -> { `webui`, `lava`, `immich` }

- 所有对外 HTTP/HTTPS 接入点由 Nginx/Traefik/Kong 统一处理并做 TLS。
- 推荐在 Gateway 层实施速率限制、审计、WAF 规则以及灰度发布控制。

---

## 关键避坑

- 版本锁定：Immich、Lava 与 WebUI 均要 pin 版本；避免 `latest`。
- 权限（UID/GID）：宿主机卷权限必须与容器内运行用户相匹配。
- 资源隔离：Image processing（Immich）应受限 CPU/Memory，防止影响 Lava 的交易处理。
- JWT 管理：在生产中使用 KMS 或 secrets 管理，避免明文写在 `.env`。

---

## 参考部署示例

参见仓库 `deploy/immich-merged/docker-compose.yml` 与 `deploy/immich-merged/nginx.conf`。

---

文档路径：docs/immich-merged-architecture.md
