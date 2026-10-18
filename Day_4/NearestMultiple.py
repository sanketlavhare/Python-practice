
def roundToNearest(s: str) -> str:
    n = int(s)
    lower = (n // 10) * 10
    upper = lower + 10

    if n - lower <= upper - n:
        return str(lower)
    else:
        return str(upper)
