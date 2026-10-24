def anagram(n1: int, n2: int) -> bool:
    return sorted(str(n1)) == sorted(str(n2))
print(anagram(1122, 2211))