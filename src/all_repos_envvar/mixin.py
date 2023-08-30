from __future__ import annotations

from pathlib import Path
from typing import Any

import environs


class GitHubEnvMixin:
    """Base mixin with logic to read .env file."""

    def __new__(cls, *args: Any, **kwargs: Any):  # type: ignore[no-untyped-def]
        """Read .env file and pass it the base class as api_key argument."""
        env = environs.Env()
        env_file_path = Path() / ".env"
        env.read_env(str(env_file_path))
        api_key = env("GITHUB_API_KEY", None)
        if api_key:
            kwargs.setdefault("api_key", api_key)
        return super().__new__(cls, *args, **kwargs)
