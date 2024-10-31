import os
from collections.abc import Generator
from pathlib import Path

import pytest


@pytest.fixture
def workspace(tmp_path: Path) -> Generator[Path, None, None]:
    """Fixture to change the current directory to a temporary one."""
    cwd = os.getcwd()
    os.chdir(tmp_path)
    yield tmp_path
    os.chdir(cwd)
