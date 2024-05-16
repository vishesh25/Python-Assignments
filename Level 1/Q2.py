user_input = input("Enter any string: ")

alpha = 0
digit = 0

for i in user_input:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        alpha += 1

print(f"Alphabets: {alpha} & Number : {digit}")