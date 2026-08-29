# xswitch · 保护版

xswitch 的**源码保护分发版本**：核心逻辑已编译为二进制扩展模块，入口脚本保持源码可编辑。

> 跨 AI 编码助手（Codex / Qoder / WorkBuddy）的会话聚合与无缝切换中间件。

[English](README_EN.md) | 简体中文

> 如果需要源码，请在本项目 Post 你的研究方向。

## 目录结构

```
xswitch/
├── xswitch.py                          入口，源码 331B（可自由编辑）
├── xswitch.json                        配置
├── README.md
└── xswitch/
    └── __init__.cp39-win_amd64.pyd     编译的包，649K（二进制，不可读）
```

## 运行

> ⚠️ **必须用 Python 3.9。** `.pyd` 的 `cp39` 后缀与 Python 版本绑定，
> 其他版本（如系统默认的 3.13）无法加载。

```bat
cd C:\Users\PC\WorkBuddy\2026-08-28-10-20-52\xswitch
D:\Python\Python39\python.exe xswitch.py xw
```

浏览器打开 <http://127.0.0.1:8787/xw>

## 命令

| 命令 | 说明 |
|------|------|
| `xswitch.py list` | 列出所有会话 |
| `xswitch.py show <id>` | 查看会话全文 |
| `xswitch.py search <关键词>` | 跨 app 全文检索 |
| `xswitch.py switch <id> --to <app>` | 生成切换交接简报（复制到剪贴板）|
| `xswitch.py status` | 显示各 app 检测状态与计数 |
| `xswitch.py serve` | 启动 Web UI（<http://127.0.0.1:8787>）|
| `xswitch.py xw` | 启动 **Codex⇄WorkBuddy 双向接力**界面（推荐）|

## 特性

- **零第三方依赖**：纯 Python 标准库，不装任何包。
- **无缓存**：每次请求实时重扫磁盘，所见即最新（全量约 10–15 秒）。
- **会话标题精准**：Codex 会话名取自 `~/.codex/state_5.sqlite`，实测 144/144 命中。
- **分页加载**：列表默认每页 20 条，会话再多也不卡。
- **双向接力**：Codex ⇄ WorkBuddy 一键生成交接简报并复制到剪贴板。

## 本机数据规模（参考）

```
Codex      146 会话   ~/.codex/sessions
WorkBuddy  174 会话   ~/.workbuddy/projects
────────────────────────────────────
合计       320 会话
```

## 与源码版的区别

| | 源码版 | 保护版 |
|---|---|---|
| 入口 `xswitch.py` | 源码 | 源码（可编辑）|
| `xswitch/` 包 | `.py` 源码 | `.pyd` 二进制（不可读）|
| Python 版本 | 3.8+ 任意 | **仅 3.9** |
| 修改核心逻辑 | 直接改 `.py` | 需回到源码版重新编译 |

## 配置

编辑 `xswitch.json` 可覆盖各 app 的会话目录、启停与端口：

```json
{
  "apps": {
    "codex":     { "enabled": true, "path": null },
    "qoder":     { "enabled": true, "path": null },
    "workbuddy": { "enabled": true, "path": null }
  },
  "demo_fallback": true,
  "server": { "host": "127.0.0.1", "port": 8787 }
}
```

## 重新编译

核心逻辑有改动时，回源码版目录重新编译：

```bash
cd C:\Users\PC\WorkBuddy\2026-08-28-10-20-52\2026-08-28-xswitch
rm -f xswitch/*.pyd && rm -rf xswitch/xswitch.build
python -m nuitka --module --output-dir=<保护版目录> --include-package=xswitch xswitch
```

> 编译前务必清理源码目录的旧 `.pyd` / `.build`，否则 Nuitka 会报
> `Cannot include extension module 'xswitch.xswitch'`，且产出的 `.pyd` 不含子模块。
</content>
</invoke>
