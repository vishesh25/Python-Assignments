def is_perfect_number(n):
    if n <= 0:
        return False
    
    sum_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i
    
    return sum_divisors == n

number = int(input("Enter a number: "))
if is_perfect_number(number):
    print("Yes")
else:
    print("No")
