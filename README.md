# Travel Agent

[![CI](https://github.com/pawelchoinski/travel-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/pawelchoinski/travel-agent/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/pawelchoinski/travel-agent/branch/main/graph/badge.svg)](https://codecov.io/gh/pawelchoinski/travel-agent)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![ty](https://img.shields.io/badge/type--checked-ty-blue?labelColor=orange)](https://github.com/astral-sh/ty)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/pawelchoinski/travel-agent/blob/main/LICENSE)
[![Renovate](https://img.shields.io/badge/renovate-enabled-brightgreen.svg?logo=renovate)](https://renovateapp.com/)

AI powered travel agent

## Features

- Fast and modern Python toolchain using Astral's tools (uv, ruff, ty)
- Type-safe with full type annotations
- Command-line interface built with Typer
- Comprehensive documentation with MkDocs — [View Docs](https://pawelchoinski.github.io/travel-agent/)

## Installation

```bash
pip install travel_agent
```

Or using uv (recommended):

```bash
uv add travel_agent
```

## Quick Start

```python
import travel_agent

print(travel_agent.__version__)
```

### CLI Usage

```bash
# Show version
travel_agent --version

# Say hello
travel_agent hello World
```

## Development

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) for package management

### Setup

```bash
git clone https://github.com/pawelchoinski/travel-agent.git
cd travel-agent
make install
```

### Running Tests

```bash
make test

# With coverage
make test-cov

# Across all Python versions
make test-matrix
```

### Code Quality

```bash
# Run all checks (lint, format, type-check)
make verify

# Auto-fix lint and format issues
make fix
```

### Prek

```bash
prek install
prek run --all-files
```

### Documentation

```bash
make docs-serve
```
## Dependency Updates

This project uses [Renovate](https://renovateapp.com/) to keep dependencies up to date automatically. Renovate will open pull requests when new versions of dependencies are available.

To enable it, install the [Renovate GitHub App](https://github.com/apps/renovate) and grant it access to this repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
