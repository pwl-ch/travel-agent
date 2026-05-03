import os
from pathlib import Path

def append_if_missing(file_path: Path, lines: list[str]):
    """Appends lines to a file only if they don't already exist."""
    existing_content = ""
    if file_path.exists():
        existing_content = file_path.read_text()
    
    # Normalize existing lines for comparison
    existing_lines_set = {line.strip() for line in existing_content.splitlines()}
    
    to_append = []
    for line in lines:
        if line.strip() and line.strip() not in existing_lines_set:
            to_append.append(line)
    
    if to_append:
        with open(file_path, "a") as f:
            # Ensure we start on a new line if file isn't empty
            if existing_content and not existing_content.endswith("\n"):
                f.write("\n")
            f.write("\n".join(to_append) + "\n")
        print(f"➕ Added {len(to_append)} lines to {file_path}")
    else:
        print(f"✅ {file_path} is already up to date.")

def create_missing_structure():
    # 1. Directories
    folders = [
        "workflows", "tools", "src/logic", "src/tools", "scripts", 
        "docs", "tests", "flowise_data", "logs/flowise", "logs/engine"
    ]
    for folder in folders:
        Path(folder).mkdir(parents=True, exist_ok=True)
    print("📂 Directory structure verified.")

    # 2. .gitignore updates
    git_ignore_lines = [
        ".env", "__pycache__/", ".venv/", "flowise_data/", "logs/", "*.log"
    ]
    append_if_missing(Path(".gitignore"), git_ignore_lines)

    # 3. .env.example (Safe Generation)
    env_lines = [
        "# FLOWISE CONFIG",
        "PORT=3000",
        "DATABASE_TYPE=sqlite",
        "DATABASE_PATH=/root/.flowise",
        "APIKEY_PATH=/root/.flowise",
        "LOG_LEVEL=debug",
        "",
        "# ENGINE CONFIG",
        "ENGINE_PORT=8000",
        "PYTHON_LOG_LEVEL=INFO",
        "FLOWISE_API_URL=http://flowise:3000/api/v1",
        "LOG_PATH=./logs"
    ]
    
    env_example = Path(".env.example")
    append_if_missing(env_example, env_lines)
    
    # Create .env from .env.example if .env doesn't exist at all
    if not Path(".env").exists() and env_example.exists():
        Path(".env").write_text(env_example.read_text())
        print("📝 Created .env from .env.example")

if __name__ == "__main__":
    create_missing_structure()