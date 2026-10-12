# Clawd Studio

一个用 Claude API 构建的多 Agent 内容生产系统，负责运营像素 AI 角色 **LgClawd** 的抖音 / TikTok 账号：
选题 → 分镜 → 渲染 → 自动质检 → 人工审核 → 发布。

> 状态：阶段 0（搭建中）。完整路线见 [docs/PLAN.md](docs/PLAN.md)。

## 目录结构

```
clawd-studio/
├── backend/          Python 后端（FastAPI + Claude API）
│   ├── app/          服务代码
│   ├── scripts/      一次性脚本（如 hello_claude.py）
│   └── tests/
├── renderer/         Remotion 渲染器（阶段 1 并入）
└── docs/             计划和设计文档
```

## 本地运行（后端）

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate          # macOS / Linux: source .venv/bin/activate
pip install -e ".[dev]"
copy .env.example .env          # 然后在 .env 里填 ANTHROPIC_API_KEY
pytest                          # 跑测试
uvicorn app.main:app --reload   # 启动服务，打开 http://127.0.0.1:8000/health
python scripts/hello_claude.py  # 第一次调用 Claude
```
