import math

def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)

number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))

result = lcm(number1, number2)

print(f"LCM of {number1} and {number2} is: {result}")
