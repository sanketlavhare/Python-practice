numbers = [10, 15, 20, 25, 30, 35]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even count:", even_count)
print("Odd count:", odd_count)