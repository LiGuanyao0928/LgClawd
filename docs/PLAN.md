# LgClawd 开发计划

用 Claude API 写一个多 Agent 内容生产系统，运营真实账号 LgClawd（抖音 / TikTok）：
选题 → 分镜 → 渲染 → 自动质检 → 人工审核 → 发布。

节奏：每周约 10 小时。核心代码自己写，Claude 负责讲设计和 code review。

对照的六条标准：①解决真实问题 ②后端工程 ③任务规划 ④上下文工程 ⑤可观测与评估 ⑥人机协同

---

## 阶段 0｜准备（第 1 周）
- [x] 装 Git，初始化仓库（PortableGit 2.56，在 `D:\claude code\tools\PortableGit`）
- [x] 第一次提交
- [x] Python 3.12 虚拟环境 + FastAPI 骨架，`/health` 接口和测试通过
- [ ] 在 Anthropic Console 开 API Key，设每月花费上限
- [ ] 跑通 `scripts/hello_claude.py`：第一次调用 Claude，打印花了多少钱
- [x] 建 GitHub 仓库并推送：https://github.com/LiGuanyao0928/LgClawd

## 阶段 1｜分镜 JSON → 视频（第 2–3 周）⭐
- [ ] 把现有 Remotion 项目（`D:\claude code\douyin`）并入 `renderer/`
- [ ] 整理场景库：Caption / Bubble / Notebook / IdCard / List …
- [ ] 用 Pydantic 定义分镜结构，导出 JSON Schema
- [ ] Remotion 只保留一个通用模板，按 JSON 渲染（`calculateMetadata` 算时长）
- [ ] 验收：第 1 期改写成 JSON，渲染结果和原版一致

## 阶段 2｜跑通一个 Agent（第 4–5 周）
- [ ] 编剧 Agent：选题 + 角色设定 + 场景库 → 结构化输出得到分镜（`client.messages.parse`）
- [ ] 渲染 Worker：调用 Remotion 渲染出 MP4
- [ ] 审片：渲染关键帧，用 Claude 看图检查文字溢出、遮挡、隐私问题
- [ ] 每次调用记录 `usage`，算出单期成本
- [ ] 验收：`make-episode "strawberry"` 一条命令出成片 + 质检报告

## 阶段 3｜后端 + 人机协同（第 6–7 周）→ ②⑥
- [ ] FastAPI：创建一期、查进度、通过 / 打回（带修改意见）、按意见重做
- [ ] 任务队列：先用数据库实现，加一个 Worker 进程
- [ ] 审核网页：看成片和文案，点「通过」才算定稿
- [ ] 鉴权 + 操作日志；发布、回复评论都必须人工确认

## 阶段 4｜多 Agent + 上下文工程（第 8–9 周）→ ③④
- [ ] 选题 Agent：读评论 → 挑出点单 / 提问 / 出题，去重排序，过滤违规和隐私
- [ ] 编剧 / 审片 / 运营（中英文标题、文案、标签）Agent
- [ ] 调度器：拆解任务，失败重试或回退
- [ ] 上下文：角色设定 + 场景库走 prompt caching；长期记忆（往期摘要、哪些效果好）
- [ ] 护栏：禁止话题清单做成规则检查，写测试覆盖

## 阶段 5｜可观测 + 评估（第 10 周）→ ⑤
- [ ] 追踪：每次运行 / 每个 Agent / 每次调用的模型、token、耗时、成本、成败
- [ ] 评估集：20 个选题，每改一次 prompt 跑一遍（合法率、渲染成功率、护栏违规数、评分）
- [ ] 数据回流：播放、点赞、完播率接回来，作为选题参考

## 阶段 6｜上线 + 沉淀（持续）
- [ ] 每周定时运行，账号持续更新
- [ ] README：架构图、设计决策、成本与质量数据
- [ ] 2 分钟演示视频（用系统自己生成）

---

## 成本备忘
- 默认模型 `claude-opus-5-5`：输入 $4 / 输出 $20（每百万 token），缓存读取 $0.20
- API 按量计费，和 Claude 订阅是两回事。估算一期 $0.3–0.6，以阶段 2 的实测为准
