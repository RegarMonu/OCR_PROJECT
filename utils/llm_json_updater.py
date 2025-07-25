import json
from pathlib import Path

def save_to_json(path, data: dict):
    path = Path(path)  # Ensure it's a Path object
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
