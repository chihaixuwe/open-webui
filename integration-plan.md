# Deepay AI 图像平台 - 整合方案

## 整合架构

本项目将 **Open WebUI** 和 **Immich** 合并为一个统一的平台。

---

## 1. 项目结构

```
deepay-ai-platform/
├── frontend/                  # 前端 (基于 Open WebUI + Immich)
│   ├── src/
│   │   ├── lib/
│   │   │   ├── components/
│   │   │   │   ├── chat/      # Open WebUI 聊天组件
│   │   │   │   └── gallery/   # Immich 图库组件
│   │   │   └── stores/
│   │   └── routes/
│   │       ├── +layout.svelte
│   │       ├── +page.svelte    # 首页 (聊天 + 图库)
│   │       ├── chat/
│   │       └── gallery/
│   ├── static/
│   └── package.json
│
└── backend/                   # 后端 (Laravel)
    └── ... (现有的 Laravel 项目)
```

---

## 2. 功能模块

### 首页 (/ 或 /chat)
- **左侧**: 聊天界面 (Open WebUI)
- **右侧**: 图库面板 (Immich) - 可展开/收起

### 聊天页面 (/chat)
- 纯聊天界面 (Open WebUI)
- 支持 AI 对话、代码执行、文件上传等

### 图库页面 (/gallery)
- 纯图库界面 (Immich)
- 支持图片管理、相册、标签等

### 功能特点
- ✅ AI 聊天 (Open WebUI)
- ✅ 图库管理 (Immich)
- ✅ 统一用户认证
- ✅ 统一数据存储
- ✅ 响应式设计

---

## 3. 技术栈

### 前端
- SvelteKit
- Tailwind CSS
- Open WebUI 组件
- Immich 图库组件

### 后端
- Laravel 11+
- 现有业务逻辑
- AI API 集成
- 文件存储

---

## 4. 实现步骤

### 阶段 1: 项目结构建立
- [x] 创建项目文件夹
- [x] 复制 Open WebUI 核心文件
- [x] 创建整合方案文档

### 阶段 2: 前端整合
- [ ] 合并 Open WebUI 和 Immich 组件
- [ ] 创建统一的布局
- [ ] 实现路由和导航
- [ ] 测试组件兼容性

### 阶段 3: 后端整合
- [ ] 统一用户认证
- [ ] 整合文件存储
- [ ] 实现 API 接口
- [ ] 数据迁移和同步

### 阶段 4: 测试和优化
- [ ] 功能测试
- [ ] 性能优化
- [ ] UI/UX 优化
- [ ] 文档完善

---

## 5. 文件迁移清单

### 从 Open WebUI 复制
- ✅ `src/lib/components/chat/` - 聊天组件
- ✅ `src/lib/stores/` - 状态管理
- ✅ `src/lib/apis/` - API 调用
- ✅ `src/routes/` - 路由和布局
- ✅ `static/` - 静态资源
- ✅ `package.json` - 依赖配置

### 从 Immich 复制
- [ ] `src/lib/components/shared-components/gallery-viewer/` - 图库查看器
- [ ] `src/lib/components/assets/` - 资源组件
- [ ] `src/lib/components/asset-viewer/` - 资源查看器
- [ ] `src/lib/managers/` - 管理器
- [ ] `src/lib/utils/` - 工具函数

---

## 6. 核心集成点

### 1. 布局整合
- 统一的侧边栏
- 顶部导航栏
- 可切换的图库面板
- 响应式布局

### 2. 状态管理
- 统一的用户状态
- 聊天状态
- 图库状态
- 全局通知系统

### 3. API 整合
- 统一的认证机制
- 聊天 API (OpenAI)
- 图库 API (Immich)
- 文件上传 API

### 4. 数据库整合
- 用户表 (统一)
- 聊天表 (Open WebUI)
- 资源表 (Immich)
- 关联表

---

## 7. 下一步行动

1. **确认整合方案** - 确认这个架构是否符合需求
2. **开始前端整合** - 合并组件和布局
3. **后端 API 开发** - 创建统一的 API 接口
4. **测试和迭代** - 逐步完善功能

---

**注意**: 这是一个复杂的整合项目，建议分阶段逐步实现，确保每个阶段都稳定可用。
