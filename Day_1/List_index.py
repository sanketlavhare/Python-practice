#Insert a number in a list at 6th position this number must be one third of number stored at 4th position

numbers = [10, 20, 30, 60, 80, 100]

num = numbers[3]//3
numbers.insert(4,num)

print(numbers)