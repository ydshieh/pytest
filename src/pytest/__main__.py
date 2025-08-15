"""The pytest entry point."""

from __future__ import annotations

import pytest
import sys


if __name__ == "__main__":

    code = pytest.console_main()
    print(f"pytest/__main__.py::lineno=9::__main__ | `pytest.console_main()` returns {code}")

    import os
    os.system("mkdir mem_info")
    os.system("ps aux --sort pmem > mem_info/mem_info_1.txt && sleep 10")
    os.system("ps aux --sort pmem")

    pid = os.getpid()
    print(pid)
    
    sys.stdout.flush()

    # import os
    # os._exit(code)

    raise SystemExit(code)
