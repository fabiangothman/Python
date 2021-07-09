def greet(name="none"):
    print(f"waving to {name}")
greet("Fabian")
greet()

def sum(num1=0, num2=0):
    return num1+num2
print(sum(8, 5))

#Lambda functions (one expression)
res = lambda num1, num2: num1-num2
print(res(8, 5))