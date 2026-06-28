import asyncio
import time


class TTLCache:
    """An async cache that fetches a value on miss and caches it for `ttl` seconds."""

    def __init__(self, ttl: float):
        self._ttl = ttl
        self._store: dict[str, tuple[float, object]] = {}

    async def get(self, key: str, fetch):
        entry = self._store.get(key)
        if entry and entry[0] > time.monotonic():
            return entry[1]
        async with asyncio.Lock():
            value = await fetch()
            self._store[key] = (time.monotonic() + self._ttl, value)
            return value
