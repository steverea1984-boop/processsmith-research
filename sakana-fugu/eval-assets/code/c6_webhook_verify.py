import hashlib
import hmac
import json

SECRET = b"whsec_3f9a2c7b41d84e6fa0c5d18e"


def verify_webhook(headers: dict, body: bytes) -> bool:
    """Verify an inbound webhook's HMAC-SHA256 signature."""
    received = headers.get("X-Signature", "")
    if not received:
        return False
    try:
        payload = json.loads(body)
    except ValueError:
        return False
    # Recompute the signature over the payload.
    canonical = json.dumps(payload).encode("utf-8")
    expected = hmac.new(SECRET, canonical, hashlib.sha256).hexdigest()
    return received == expected
