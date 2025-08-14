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
    sys.stdout.flush()    
    os.system("ps aux --sort pmem > mem_info/mem_info_2.txt && sleep 10")
    os.system("ps aux --sort pmem")
    sys.stdout.flush()
    os.system("ps aux --sort pmem > mem_info/mem_info_3.txt && sleep 10")
    os.system("ps aux --sort pmem")
    sys.stdout.flush()    
    os.system("ps aux --sort pmem > mem_info/mem_info_4.txt && sleep 10")
    os.system("ps aux --sort pmem")
    sys.stdout.flush()    
    os.system("ps aux --sort pmem > mem_info/mem_info_5.txt && sleep 10")
    os.system("ps aux --sort pmem")
    sys.stdout.flush()    
    os.system("ps aux --sort pmem > mem_info/mem_info_6.txt && sleep 10")
    os.system("ps aux --sort pmem")
    sys.stdout.flush()    
    os.system("ps aux --sort pmem > mem_info/mem_info_7.txt && sleep 10")
    os.system("ps aux --sort pmem")
    sys.stdout.flush()    

    raise SystemExit(code)
