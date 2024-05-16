def get_user_input(prompt):
    return input(prompt)

def create_user_account():
    username = get_user_input("Enter username: ")
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        password = get_user_input("Enter password: ")
        password_confirm = get_user_input("Re-type password: ")

        if password == password_confirm:
            print("Account created successfully!")
            return username, password 
        else:
            print("Passwords do not match. Please try again.")
            attempts += 1

    print("You have exceeded the maximum number of attempts.")
    return None

def login(username, password):
    entered_username = get_user_input("Enter your username: ")
    entered_password = get_user_input("Enter your password: ")

    if entered_username == username and entered_password == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")


user_info = create_user_account()
if user_info:
    login(user_info[0], user_info[1])
