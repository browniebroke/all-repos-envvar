import os
from unittest import mock

import all_repos.push.github_pull_request

from all_repos_envvar import push


class TestSettings:
    def test_key_from_param(self):
        settings = push.Settings(
            api_key="notsecret",
            username="browniebroke",
        )
        assert settings.api_key == "notsecret"

    @mock.patch.dict(os.environ, {"GITHUB_API_KEY": "notsecret"})
    def test_key_from_env(self):
        settings = push.Settings(
            username="browniebroke",
        )
        assert settings.api_key == "notsecret"

    @mock.patch.dict(os.environ, {"GITHUB_API_KEY": "ignored"})
    def test_key_from_both(self):
        settings = push.Settings(
            api_key="realone",
            username="browniebroke",
        )
        assert settings.api_key == "realone"

    def test_env_file(self, workspace):
        env_file = workspace / ".env"
        env_file.write_text("GITHUB_API_KEY=notsecret\n")
        settings = push.Settings(
            username="browniebroke",
        )
        assert settings.api_key == "notsecret"


def test_push_same_as_base():
    assert hasattr(push, "push")
    assert callable(push.push)
    assert push.push == all_repos.push.github_pull_request.push
