
def multiplicationTable(n: int, limit: int) -> list[int]:
    result = []
    for i in range(1, limit + 1):
        result.append(n * i)
    return result
