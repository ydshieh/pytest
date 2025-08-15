"""The pytest entry point."""

from __future__ import annotations

import pytest


if __name__ == "__main__":
    import os
    os._exit(pytest.console_main())
