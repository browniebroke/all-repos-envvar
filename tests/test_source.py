import os
from unittest import mock

import all_repos.source.github

from all_repos_envvar import source


class TestSettings:
    def test_key_from_param(self):
        settings = source.Settings(
            api_key="notsecret",
            username="browniebroke",
        )
        assert settings.api_key == "notsecret"

    @mock.patch.dict(os.environ, {"GITHUB_API_KEY": "notsecret"})
    def test_key_from_env(self):
        settings = source.Settings(
            username="browniebroke",
        )
        assert settings.api_key == "notsecret"

    @mock.patch.dict(os.environ, {"GITHUB_API_KEY": "ignored"})
    def test_key_from_both(self):
        settings = source.Settings(
            api_key="realone",
            username="browniebroke",
        )
        assert settings.api_key == "realone"


def test_list_repos_same_as_base():
    assert hasattr(source, "list_repos")
    assert callable(source.list_repos)
    assert source.list_repos == all_repos.source.github.list_repos
