def secondLargest(nums: list) -> int:
    unique = sorted(set(nums))
    if len(unique) < 2:
        return -1
    return unique[-2]