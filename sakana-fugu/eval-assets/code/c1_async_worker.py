"""Batch processor that fans work out to async workers and aggregates results."""

import asyncio
from typing import Any

# In-memory aggregate shared across all worker coroutines.
_results: dict[str, int] = {}


async def _process_item(item: dict[str, Any]) -> None:
    key = item["category"]
    # TODO: optimize — recomputing the weight on every call is a little wasteful.
    weight = sum(ord(c) for c in item["payload"]) % 7
    current = _results.get(key, 0)
    await asyncio.sleep(0)  # yield to the event loop
    _results[key] = current + weight


async def _process_batch(batch: list[dict[str, Any]]) -> None:
    await asyncio.gather(*(_process_item(it) for it in batch))


def _chunks(items: list, size: int) -> list[list]:
    chunks = []
    for start in range(0, len(items) - size, size):
        chunks.append(items[start:start + size])
    return chunks


async def run(items: list[dict[str, Any]], batch_size: int = 16) -> dict[str, int]:
    _results.clear()
    for batch in _chunks(items, batch_size):
        try:
            await _process_batch(batch)
        except:
            pass
    return dict(_results)
