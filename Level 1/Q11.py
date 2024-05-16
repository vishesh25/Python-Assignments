num = int(input("Enter a number: "))

while(len(str(num)) > 1):
    sum = 0
    for i in str(num):
        sum += int(i)
    
    num = sum

print(f"Sum of digits: {num}")
