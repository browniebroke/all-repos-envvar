# all-repos-envvar

<p align="center">
  <a href="https://github.com/browniebroke/all-repos-envvar/actions/workflows/ci.yml?query=branch%3Amain">
    <img src="https://img.shields.io/github/actions/workflow/status/browniebroke/all-repos-envvar/ci.yml?branch=main&label=CI&logo=github&style=flat-square" alt="CI Status" >
  </a>
  <a href="https://codecov.io/gh/browniebroke/all-repos-envvar">
    <img src="https://img.shields.io/codecov/c/github/browniebroke/all-repos-envvar.svg?logo=codecov&logoColor=fff&style=flat-square" alt="Test coverage percentage">
  </a>
</p>
<p align="center">
  <a href="https://github.com/astral-sh/uv">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json" alt="uv">
  </a>
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff">
  </a>
  <a href="https://github.com/pre-commit/pre-commit">
    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square" alt="pre-commit">
  </a>
</p>
<p align="center">
  <a href="https://pypi.org/project/all-repos-envvar/">
    <img src="https://img.shields.io/pypi/v/all-repos-envvar.svg?logo=python&logoColor=fff&style=flat-square" alt="PyPI Version">
  </a>
  <img src="https://img.shields.io/pypi/pyversions/all-repos-envvar.svg?style=flat-square&logo=python&amp;logoColor=fff" alt="Supported Python versions">
  <img src="https://img.shields.io/pypi/l/all-repos-envvar.svg?style=flat-square" alt="License">
</p>

---

**Source Code**: <a href="https://github.com/browniebroke/all-repos-envvar" target="_blank">https://github.com/browniebroke/all-repos-envvar</a>

---

An all-repos extension to read values from environment variables.

> [!IMPORTANT]
> As of [all-repos v1.25](https://github.com/asottile/all-repos/releases/tag/v1.25.0), you may not need this package, see [section below](#why)

## Installation

Install this via pip (or your favourite package manager):

`pip install all-repos-envvar`

## Usage

This library should be installed alongside `all-repos` so that it's findable at import time. It provides a custom `source` and `push` to get the GitHub API key from an environment variable `GITHUB_API_KEY` (reading from and `.env` file is also supported), allowing you to omit it from the config:

```json
{
  "output_dir": "output",
  "source": "all_repos_envvar.source",
  "source_settings": {
    "username": "browniebroke"
  },
  "push": "all_repos_envvar.push",
  "push_settings": {
    "username": "browniebroke"
  }
}
```

The source module extends `all_repos.source.github` and the push module extends `all_repos.push.github_pull_request`.

## Why

I wanted this feature, but at the time, it looked like [it would never be implemented in the main repo](https://github.com/asottile/all-repos/issues/79), hence this little extension. Since then, the author of all-repos apparently changed their mind and support for reading from environment variable [was added in early 2023](https://github.com/asottile/all-repos/pull/275), and it's now included since release v1.25.0.

The only extra feature that this package provides is to read from `.env` file, but this can be achieved by more general solutions like [`direnv`](https://direnv.net).

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- prettier-ignore-start -->
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://browniebroke.com/"><img src="https://avatars.githubusercontent.com/u/861044?v=4?s=80" width="80px;" alt=""/><br /><sub><b>Bruno Alla</b></sub></a><br /><a href="https://github.com/browniebroke/all-repos-envvar/commits?author=browniebroke" title="Code">💻</a> <a href="#ideas-browniebroke" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/browniebroke/all-repos-envvar/commits?author=browniebroke" title="Documentation">📖</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
<!-- prettier-ignore-end -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

## Credits

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[browniebroke/cookiecutter-pypackage](https://github.com/browniebroke/cookiecutter-pypackage)
project template.
