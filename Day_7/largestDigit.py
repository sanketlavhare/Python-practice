def returnLargestDigit(n):
    largest = 0
    while n > 0:
        digit = n % 10
        if digit > largest:
            largest = digit 

        n = n // 10
    return largest 

print(returnLargestDigit(89))