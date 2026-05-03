# Set shell to zsh for Mac compatibility
set shell := ["zsh", "-cu"]

# Default command: list all available recipes
default:
    @just --list

# --- Project Initialization ---

init:
    uv run python scripts/init_project.py

install:
    uv sync --all-groups

# --- Docker & Flowise ---

# Check if Ollama is responsive on the local network
check-ollama:
    @echo "🔍 Checking Ollama status..."
    @curl -fsSL http://localhost:11434/api/tags > /dev/null || (echo "❌ Ollama is not running! Please start it at http://localhost:11434 before launching." && exit 1)
    @echo "✅ Ollama is responsive."

# Start Flowise and Engine, waiting for them to be healthy
up:
    @echo "🚀 Starting containers..."
    docker compose up -d --wait
    @echo "✨ Environment is healthy and running."

down:
    docker compose down

# Clean logs from both the local engine and the shared Flowise folder
clean-logs:
    rm -rf logs/engine/*
    rm -rf ../shared-flowise/logs/flowise/*
    @echo "🧹 Logs cleared (Local and Shared)."

sync:
    uv run python scripts/sync_flowise.py

# --- QA & Testing ---

verify: lint format-check type-check

fix:
    uv run ruff check --fix .
    uv run ruff format .

lint:
    uv run ruff check .

format-check:
    uv run ruff format --check .

type-check:
    uv run ty check

test:
    uv run pytest tests/ -v