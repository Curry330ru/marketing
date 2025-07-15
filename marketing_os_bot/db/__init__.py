import json
from pathlib import Path

DB_PATH = Path(__file__).with_name('users.json')

if not DB_PATH.exists():
    DB_PATH.write_text('{}')

def load_users() -> dict:
    return json.loads(DB_PATH.read_text())

def save_users(data: dict) -> None:
    DB_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2))
