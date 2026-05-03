import httpx
import json
from pathlib import Path

# Config
BASE_URL = "http://localhost:3000/api/v1"
FLOWS_DIR = Path("./workflows")

def sync():
    FLOWS_DIR.mkdir(exist_ok=True)
    with httpx.Client() as client:
        # Exporting Flows
        flows = client.get(f"{BASE_URL}/chatflows").json()
        for flow in flows:
            detail = client.get(f"{BASE_URL}/chatflows/{flow['id']}").json()
            filename = FLOWS_DIR / f"{flow['name'].replace(' ', '_').lower()}.json"
            with open(filename, "w") as f:
                json.dump(detail, f, indent=2)
            print(f"Exported: {flow['name']}")

if __name__ == "__main__":
    sync()