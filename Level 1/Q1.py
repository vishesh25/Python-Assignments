while(True):

    user_input = int(input("Enter a number: "))

    if user_input % 3 == 0 and user_input % 5 == 0:
        print("Consultadd - Python Training")
    elif user_input % 3 == 0:
        print("Consultadd")
    elif user_input % 5 == 0:
        print("Python Training")
    else:
        print("Given number is neither divisible by 3 nor 5.")
    
    if (input("Do you want to continue?(Y/N)").lower() == 'y'):
        continue
    else:
        break