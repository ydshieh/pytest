"""The pytest entry point."""

from __future__ import annotations

import pytest
import sys


if __name__ == "__main__":

    code = pytest.console_main()
    print(f"pytest/__main__.py::lineno=9::__main__ | `pytest.console_main()` returns {code}")

    sys.stdout.flush()
    raise SystemExit(code)
