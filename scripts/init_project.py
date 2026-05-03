import os
from pathlib import Path

def append_if_missing(file_path: Path, lines: list[str]):
    existing_content = ""
    if file_path.exists():
        existing_content = file_path.read_text()
    
    existing_lines_set = {line.strip() for line in existing_content.splitlines()}
    to_append = [l for l in lines if l.strip() and l.strip() not in existing_lines_set]
    
    if to_append:
        with open(file_path, "a") as f:
            if existing_content and not existing_content.endswith("\n"):
                f.write("\n")
            f.write("\n".join(to_append) + "\n")
        print(f"➕ Updated {file_path}")

def setup():
    # Define the sibling shared directory
    shared_base = Path("../shared-flowise")
    
    # 1. Create Folders (Local and Shared)
    local_folders = ["workflows", "tools", "src/logic", "src/tools", "scripts", "docs", "tests", "logs/engine"]
    shared_folders = [shared_base / "flowise_data", shared_base / "logs/flowise"]
    
    for folder in local_folders:
        Path(folder).mkdir(parents=True, exist_ok=True)
        
    for folder in shared_folders:
        folder.mkdir(parents=True, exist_ok=True)
        
    print(f"📂 Project directories verified. Shared data located at: {shared_base.resolve()}")

    # 2. Update .gitignore (Remove flowise_data as it's no longer in the project)
    append_if_missing(Path(".gitignore"), [
        ".env", "__pycache__/", ".venv/", "logs/", "*.log"
    ])

    # 3. Update .env.example
    append_if_missing(Path(".env.example"), [
        "PORT=3000",
        "DATABASE_PATH=/root/.flowise",
        "LOG_LEVEL=debug",
        "ENGINE_PORT=8000",
        "FLOWISE_API_URL=http://flowise:3000/api/v1",
        "SHARED_FLOWISE_PATH=../shared-flowise"
    ])

if __name__ == "__main__":
    setup()