# Travel Agent

AI powered travel agent

## Installation

Install using pip:

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

### Command Line Interface

Travel Agent provides a command-line interface:

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

Clone the repository and install dependencies:

```bash
git clone https://github.com/pawelchoinski/travel-agent.git
cd travel-agent
uv sync --group dev
```

### Running Tests

```bash
uv run pytest
```

### Code Quality

```bash
# Lint
uv run ruff check .

# Format
uv run ruff format .

# Type check
uv run ty check
```

### Prek Hooks

Install prek hooks:

```bash
prek install
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/pawelchoinski/travel-agent/blob/main/LICENSE) file for details.
