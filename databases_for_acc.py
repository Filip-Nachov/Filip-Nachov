# this code is 2 years old and not for usage even tho it works I made this to test uploading on github hence why I uploaded it to the special reposetory
user_data_list = []

def get_info():
    name = input("Enter your full name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    age = input("Enter your age: ")
    while True:
        try:
            age = int(age)
        except ValueError:
            print(f"The age entered is not an actual number {age}")

    passwordConfirmation = input("Confirm your password: ")

    if passwordConfirmation != password:
        print("Your passwords don't match")
    else:
        user_info = {
            'name': name,
            'email': email,
            'age': age,
            'password': password
        }
        user_data_list.append(user_info)
        print(f"Hello, {name}! You have successfully registered an account with us")
        print(f"email: {email}\nName:{name}")


# Function to log in
def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    for user in user_data_list:
        if user['email'] == email and user['password'] == password:
            print(f"Welcome back, {user['name']}!")
            return
    print("Invalid email or password. Please try again or create a new account.")

# Example usage
while True:
    print("1. Log in")
    print("0. Quit")
    print("+. Create a new account")
    choice = input("Enter your choice: ")

    if choice == '1':
        login()
    elif choice == '+':
        get_info()
    elif choice == '0':
        break
    else:
        print("Invalid choice. Please enter 1, 0, or +.")
