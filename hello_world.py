

def get_user_name():
    while True:
        user_name = input("Please enter your name: ")
        if user_name.isalpha(): 
            return user_name
        else:
            print("Invalid input. Please enter only letters.")

def greet_user(name):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    name = get_user_name()  
    greet_user(name)
