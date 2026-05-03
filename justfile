# Set shell to zsh for Mac compatibility
set shell := ["zsh", "-cu"]

# Default command: list all available recipes
default:
    @just --list

# --- Project Initialization ---

# Safely initialize or update the project structure
init:
    uv run python scripts/init_project.py

# Install all dependencies using uv
install:
    uv sync --all-groups

# --- Quality Assurance & Linting ---

# Check everything without making changes
verify: lint format-check type-check

# Automatically fix linting and formatting issues
fix:
    uv run ruff check --fix .
    uv run ruff format .

# Run ruff linter
lint:
    uv run ruff check .

# Check formatting without applying changes
format-check:
    uv run ruff format --check .

# Apply ruff formatting
format:
    uv run ruff format .

# Run type checking using the 'ty' command
type-check:
    uv run ty check

# Dependency vulnerability scanning
pysentry:
    uv run pysentry-rs

# --- Testing ---

# Run standard pytest
test:
    uv run pytest tests/ -v

# Run tests with coverage report
test-cov:
    uv run pytest --cov --cov-report=xml --cov-report=term-missing

# Run tests across all Python versions using hatch
test-matrix:
    uv run hatch test

# Run tests with coverage across all Python versions
test-matrix-cov:
    uv run hatch test --cover

# --- Agentic Workflows & Docker ---

# Start the full stack (Flowise + Engine) in the background
up:
    docker compose up -d

# Stop all running containers
down:
    docker compose down

# Sync Flowise UI workflows to the local /workflows folder
sync:
    uv run python scripts/sync_flowise.py

# Clean temporary container logs for both Flowise and the Engine
clean-logs:
    rm -rf logs/flowise/* logs/engine/*
    @echo "🧹 Logs cleared."

# --- Documentation ---

# Build documentation
docs:
    uv run mkdocs build

# Serve documentation locally
docs-serve:
    uv run mkdocs serve# Set shell to zsh for Mac compatibility
set shell := ["zsh", "-cu"]

# Default command: list all available recipes
default:
    @just --list

# --- Project Initialization ---

# Safely initialize or update the project structure
init:
    uv run python scripts/init_project.py

# Install all dependencies using uv
install:
    uv sync --all-groups

# --- Quality Assurance & Linting ---

# Check everything without making changes
verify: lint format-check type-check

# Automatically fix linting and formatting issues
fix:
    uv run ruff check --fix .
    uv run ruff format .

# Run ruff linter
lint:
    uv run ruff check .

# Check formatting without applying changes
format-check:
    uv run ruff format --check .

# Apply ruff formatting
format:
    uv run ruff format .

# Run type checking using the 'ty' command
type-check:
    uv run ty check

# Dependency vulnerability scanning
pysentry:
    uv run pysentry-rs

# --- Testing ---

# Run standard pytest
test:
    uv run pytest tests/ -v

# Run tests with coverage report
test-cov:
    uv run pytest --cov --cov-report=xml --cov-report=term-missing

# Run tests across all Python versions using hatch
test-matrix:
    uv run hatch test

# Run tests with coverage across all Python versions
test-matrix-cov:
    uv run hatch test --cover

# --- Agentic Workflows & Docker ---

# Start the full stack (Flowise + Engine) in the background
up:
    docker compose up -d

# Stop all running containers
down:
    docker compose down

# Sync Flowise UI workflows to the local /workflows folder
sync:
    uv run python scripts/sync_flowise.py

# Clean temporary container logs for both Flowise and the Engine
clean-logs:
    rm -rf logs/flowise/* logs/engine/*
    @echo "🧹 Logs cleared."

# --- Documentation ---

# Build documentation
docs:
    uv run mkdocs build

# Serve documentation locally
docs-serve:
    uv run mkdocs serve