def calculation(func):
    def calculate(a, b):
        return func(a, b)
    return calculate



@calculation
def add(a, b):
    return(a + b)

@calculation
def multiply(a,b):
    return a*b

@calculation
def divide(a,b):
    if b == 0:
        print("0 ilə əməl etmək mümkün deyil")
    else:
        return a/b

@calculation
def subtract(a,b):
    return a - b

print(add(6,5))
print(multiply(5,5))
print(divide(12,0))
print(subtract(20,5))
