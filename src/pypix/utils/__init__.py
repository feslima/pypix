from decimal import ROUND_HALF_UP, Decimal


def round_decimal(value: Decimal) -> Decimal:
    return Decimal(value.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
