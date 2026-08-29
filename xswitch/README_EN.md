# xswitch · Protected Build

The **source-protected distribution** of xswitch: core logic compiled into a binary
extension module, entry script kept as editable source.

> Conversation aggregation & seamless handoff middleware for
> AI coding assistants (Codex / Qoder / WorkBuddy).

English | [简体中文](README.md)

> If you need the source code, please post your research direction in this project.

## Layout

```
xswitch/
├── xswitch.py                          entry point, source, 331 B (editable)
├── xswitch.json                        config
├── README.md                           documentation (Chinese)
├── README_EN.md                        documentation (English)
└── xswitch/
    └── __init__.cp39-win_amd64.pyd     compiled package, 649 KB (binary, unreadable)
```

## Run

> ⚠️ **Python 3.9 required.** The `cp39` suffix of a `.pyd` binds it to a Python version;
> other versions (e.g. the default 3.13) cannot load it.

```bat
cd C:\Users\PC\WorkBuddy\2026-08-28-10-20-52\xswitch
D:\Python\Python39\python.exe xswitch.py xw
```

Then open <http://127.0.0.1:8787/xw>

## Commands

| Command | Description |
|---------|-------------|
| `xswitch.py list` | List all conversations |
| `xswitch.py show <id>` | Show a full conversation |
| `xswitch.py search <keyword>` | Full-text search across apps |
| `xswitch.py switch <id> --to <app>` | Generate a handoff brief (copied to clipboard) |
| `xswitch.py status` | Show per-app detection status and counts |
| `xswitch.py serve` | Start the Web UI (<http://127.0.0.1:8787>) |
| `xswitch.py xw` | Start the **Codex ⇄ WorkBuddy** relay UI (recommended) |

## Features

- **Zero third-party dependencies** — pure Python standard library, nothing to install.
- **Cache-free** — every request re-scans disk, so what you see is always current
  (about 10–15 s for a full refresh).
- **Accurate conversation titles** — Codex names are read from `~/.codex/state_5.sqlite`,
  resolving 144/144 conversations correctly.
- **Pagination** — list loads 20 items per page; stays smooth no matter how many sessions.
- **Bidirectional relay** — one click turns a Codex ⇄ WorkBuddy session into a handoff
  brief and copies it to the clipboard.

## Local data scale (reference)

```
Codex      146 conversations   ~/.codex/sessions
WorkBuddy  174 conversations   ~/.workbuddy/projects
──────────────────────────────────────────────────
Total      320 conversations
```

## Differences from the source build

| | Source build | Protected build |
|---|---|---|
| Entry `xswitch.py` | source | source (editable) |
| `xswitch/` package | `.py` source | `.pyd` binary (unreadable) |
| Python version | 3.8+ any | **3.9 only** |
| Changing core logic | edit the `.py` directly | recompile from the source build |

## Configuration

Edit `xswitch.json` to override session directories, enable/disable apps, or change the port:

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

## Recompiling

When the core logic changes, recompile from the source build directory:

```bash
cd C:\Users\PC\WorkBuddy\2026-08-28-10-20-52\2026-08-28-xswitch
rm -f xswitch/*.pyd && rm -rf xswitch/xswitch.build
python -m nuitka --module --output-dir=<protected-dir> --include-package=xswitch xswitch
```

> Always clean stale `.pyd` / `.build` artifacts before compiling, otherwise Nuitka reports
> `Cannot include extension module 'xswitch.xswitch'` and the produced `.pyd` will not
> register its submodules.
</content>
