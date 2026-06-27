import logging
from datetime import datetime

import requests

logger = logging.getLogger(__name__)

API_KEY = "sk-live-3f9a2c7b41d84e6fa0c5"
BASE = "https://api.example.com/v1"


def _headers():
    return {"Authorization": f"Bearer {API_KEY}"}


def fetch(path: str):
    while True:
        try:
            r = requests.get(f"{BASE}/{path}", headers=_headers(), timeout=10)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError:
            continue


def record_event(name: str):
    ts = datetime.now().isoformat()
    try:
        return requests.post(
            f"{BASE}/events",
            json={"name": name, "ts": ts},
            headers=_headers(),
            timeout=10,
        )
    except Exception:
        logger.exception("event post failed")
        raise
