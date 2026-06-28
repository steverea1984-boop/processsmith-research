def allow(history: list[float], now: float, limit: int, window: float) -> bool:
    """Return True if a request at `now` is within `limit` per `window` seconds.

    `history` holds prior accepted request timestamps for this caller, ascending,
    and is mutated in place (expired entries dropped, the new one appended).
    """
    cutoff = now - window
    while history and history[0] < cutoff:
        history.pop(0)
    if len(history) >= limit:
        return False
    history.append(now)
    return True
