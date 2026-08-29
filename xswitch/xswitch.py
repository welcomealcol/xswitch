#!/usr/bin/env python
"""项目根入口：python xswitch.py <subcommand>  或  python -m xswitch"""
# 禁止生成 .pyc 字节码缓存（避免旧缓存导致代码修改不生效）
import os
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

import sys
from xswitch.cli import main

if __name__ == "__main__":
    main(sys.argv[1:])
