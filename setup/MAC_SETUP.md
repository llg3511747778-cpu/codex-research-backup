# 在 Mac 上恢复

这份仓库保留技能、研究规则、文献索引和可读对话；不会把 Windows 软件和活跃任务迁到 Mac，也不会自动恢复 Codex 侧栏里的旧会话。

## 1. 下载

在 Mac 安装并登录 Codex，GitHub 使用自己的账号。推荐使用 GitHub Desktop 克隆私有仓库，也可运行：

```sh
git clone https://github.com/llg3511747778-cpu/codex-research-backup.git
cd codex-research-backup
```

私有仓库克隆需要本机 GitHub 身份验证；Codex 内连接 GitHub 不等于终端 Git 已登录。不要把 token 直接写进命令或 URL。

## 2. 检查，然后安装技能

以下脚本只需 Python 3 标准库。先运行 `python3 --version`；若没有 Python 3，先安装适合本机架构的 Python 3。

```sh
python3 setup/restore_skills.py --check
python3 setup/restore_skills.py
python3 setup/check_environment.py
```

默认安装常用研究技能到 `~/.agents/skills`。已经存在且内容不同的技能会跳过，避免覆盖另一台电脑已有定制；需要替换时使用 `--replace`，脚本会先备份原目录。需要安装所有已归档的非 Windows 专用技能时：

```sh
python3 setup/restore_skills.py --profile all
```

归档中保留的 Windows 专用技能不会在 Mac 安装。OpenAI 自带技能和插件缓存未打包，应在新电脑通过 Codex 正常安装/启用，并重新连接需要的服务。若技能未出现，重启 Codex。

官方技能位置：<https://learn.chatgpt.com/docs/build-skills>。

## 3. 让新对话理解之前的研究

在 Codex 打开本仓库，先让它读 `README.md`、`AGENTS.md`、`conversations/INDEX.md`，再选读相关对话与文献索引。读取全部对话通常没有必要。

`research/memory-reference` 是旧电脑记忆的只读参考导出，未自动写入 Mac 的 Codex 记忆系统。`handover/windows-snapshots` 是历史交接，可能已过期；不得凭这些快照直接启动、终止或清理仿真。

## 4. Mac 与 Windows 的分工

| 工作 | Mac 端处理方式 |
|---|---|
| 论文阅读、研究讨论、Markdown | 可使用；原 PDF 另行复制或定位 |
| CSV 图表与科学分析 | 先核验 Python 包、字体，再做一个小样验证 |
| PPT、Word、PDF | 核验对应库/转换工具和中文字体；重新检查排版 |
| SolidWorks COM / ANSYS Workbench 原有脚本 | 留在兼容的 Windows 电脑执行 |
| Fluent 结果分析 | 表格与导出数据可在 Mac 分析；当前原生 Windows 求解/登记流程继续由原电脑执行 |
| 旧会话侧栏恢复 | 本仓库不提供应用数据库迁移；通过 Markdown 接续上下文 |

不要把原 Windows `config.toml`、`auth.json`、数据库或全局 AGENTS.md 直接覆盖到 Mac。Windows 的 `D:\\`、`F:\\` 在 Mac 不存在；参照 `setup/paths.example.json` 建立本机 `local-paths.json`（已忽略，不上传），再按任务修改路径。技能保存成功并不等于该技能全部依赖已经可用。

## 5. 验收

1. `restore_skills.py --check` 返回 `archive_verified: true`。
2. Codex 能识别已安装技能；任选一个技能，能正确读取其参考文件。
3. `check_environment.py` 列出本机实际工具与缺失依赖。
4. 用一小份真实 CSV 生成带中文标签的图，检查坐标、字体和数值；做 PPT/PDF 时再分别生成一页样本。
5. 阅读一份旧对话，能正确说明研究方向与当前问题。涉及当前仿真进度时，回原电脑读取最新状态。

本仓库的导出、哈希、路径冲突检查和恢复脚本可以在 Windows 上预检；只有在你的 Mac 上完成上述步骤，才能称具体工作流已在 Mac 验收。

## 6. 两台电脑持续更新

每次开始先 `git pull`。修改资料后，检查变更，再 `git add <具体文件>`、`git commit`、`git push`。这不是自动双向同步。两边同时修改同一文件时先处理冲突，不使用强制覆盖。

当前备份为一次快照，不会自动追加以后的 Codex 对话。需要更新时重新导出，并检查凭据后再提交。原始 session 日志、图片附件、大型 CFD 场和软件安装包没有上传，仍须保留原电脑或独立备份。
