def add(x, y):
    return x + y 
def mul(x,y):
    return "Multiplication is ", x*y 
def calculate(func, x, y):
    return func(x, y)

result = calculate(add, 8, 10)
res = calculate(mul, 5, 5)
print(res)
print(result)