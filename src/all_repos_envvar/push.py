from all_repos.push import github_pull_request as base

from .mixin import GitHubEnvMixin


class Settings(GitHubEnvMixin, base.Settings):
    """Extend all_repos' Settings with our mixin."""


push = base.push
