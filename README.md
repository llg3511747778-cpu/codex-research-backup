# Codex 研究资料与技能备份

私有仓库，供 Windows 原电脑和 Mac 新电脑共享研究资料。当前为 2026-11-01 的一次导出快照。

## 在 Mac 开始

先读 [Mac 恢复与验收说明](setup/MAC_SETUP.md)。在 Codex 打开本仓库，让它读取 [AGENTS.md](AGENTS.md) 和 [对话索引](conversations/INDEX.md)，再按需阅读旧讨论。

```sh
python3 setup/restore_skills.py --check
python3 setup/restore_skills.py
python3 setup/check_environment.py
```

恢复脚本默认安装 20 个常用研究技能到 `~/.agents/skills`，先做 SHA-256 校验；现有同名定制默认跳过。全部自装技能均已归档，使用 `--profile all` 可安装非 Windows 专用技能。5 个明确 Windows 专用流程保存在归档内，Mac 不自动安装。

## 已保留的内容

| 内容 | 范围 | 入口 |
|---|---|---|
| 自装技能 | 196 个技能、3031 份文件；包含脚本/模板/参考资料，排除缓存和系统自带技能 | [技能清单](inventory/skills.json)、`archives/` |
| 可读对话 | 163 份普通及归档对话，共 5946 条用户/助手可见消息 | [对话索引](conversations/INDEX.md) |
| 规则 | 原 Windows 全局规则、项目规则及本仓库跨平台说明 | `instructions/`、[AGENTS.md](AGENTS.md) |
| 研究积累 | 旧电脑记忆文本参考、文献知识卡片/证据索引 | `research/` |
| 交接资料 | 若干仿真阶段与周报 Markdown 的历史快照 | `handover/windows-snapshots/` |
| 校验 | 技能逐文件哈希、快照范围、对话导出错误及凭据替换统计 | `inventory/` |

技能分卷是原始 ZIP 的二进制分块。恢复脚本自动按 `archives/skills-parts.json` 拼接并核对整体及每个文件的 SHA-256；无须手工解压分卷。

## 范围与限制

- 对话导出只保存可见文字；不包含工具原始调用/输出、内部推理、原始图片/音视频附件或可执行会话状态。原始 session 日志仍在 Windows 电脑，未删除、未上传。
- 下载仓库能阅读并接续研究上下文，但不能保证原对话重新出现在 Codex 侧栏。没有上传或修改应用会话数据库。
- 活跃对话仅是读取时快照，不包含随后新增的消息。本仓库不会自动追踪未来对话。
- 旧记忆是参考资料；没有自动写入新电脑记忆系统。原 Windows 规则不直接覆盖 Mac 全局配置。
- 未包含账号凭据、`auth.json`、实时 SQLite 数据库、插件缓存、软件安装包、原 PDF 库、原始大图附件、CAD/网格/Fluent 大场。文献索引和历史报告可能引用原电脑绝对路径；原 PDF 与图表另行复制后才能打开。
- 可识别凭据在备份副本中替换，原文件未改。详见 [替换记录](inventory/redactions.json)。部分匹配可能来自测试示例；这些副本用于恢复参考，仍需按任务验证脚本。
- ANSYS Workbench / SolidWorks COM / 原生 Windows 求解和登记流程继续留在兼容 Windows 主机。复制技能不安装相应软件、许可证、连接器或依赖。
- Windows 上通过的哈希和恢复预检不代表已在你的 Mac 上执行验收；Mac 的依赖、架构、中文字体及排版必须现场验证。
- 历史交接的 PID、磁盘和任务状态可能过期。读取交接不等于授权启动求解、后台监控或清理结果。

## 更新方法

两台电脑使用前先拉取，修改后检查变更、提交并上传。不要把运行中的 `.codex` 数据库目录纳入 Git 双向同步。重新导出对话时保留索引与明确的快照日期，不把历史任务状态当成实时状态。

官方技能目录与加载方式：[Build skills](https://learn.chatgpt.com/docs/build-skills)。
