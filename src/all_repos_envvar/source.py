from all_repos.source import github as base

from .mixin import GitHubEnvMixin


class Settings(GitHubEnvMixin, base.Settings):
    """Extend all_repos' Settings with our mixin."""


list_repos = base.list_repos
