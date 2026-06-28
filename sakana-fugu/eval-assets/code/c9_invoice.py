from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def split_total(total: Decimal, n: int) -> list[Decimal]:
    """Split `total` into `n` shares, each rounded to whole cents."""
    share = (total / n).quantize(CENT, rounding=ROUND_HALF_UP)
    return [share] * n


def line_tax(lines: list[Decimal], rate: Decimal) -> Decimal:
    """Total tax across line items at `rate` (e.g. Decimal('0.0825'))."""
    return sum((line * rate).quantize(CENT, rounding=ROUND_HALF_UP) for line in lines)
