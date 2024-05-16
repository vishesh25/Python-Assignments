num = int(input("Enter the number to find the factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i

print(f"Factorial of {num} is: {factorial}")