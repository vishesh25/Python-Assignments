start = int(input("Enter the start number: "))
stop = int(input("Enter the stop counter: "))

sum = 0

for i in range(start, stop + 1):
    if i % 2 != 0:
        sum += i

print(f"Sum of odd numbers: {sum}")