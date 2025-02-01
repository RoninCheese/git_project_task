# hello_world.py

# Function to get the user's name with validation
def get_user_name():
    while True:
        user_name = input("Please enter your name: ")  # Prompt for user input
        if user_name.isalpha():  # Ensure the input contains only letters
            return user_name  # Return the valid name
        else:
            print("Invalid input. Please enter only letters.")  # Error message if input is invalid
        
# Function to greet the user
def greet_user(name):
    print(f"Hello, {name}!")  # Greet the user with their name

# Main program that ties everything together
if __name__ == "__main__":
    name = get_user_name()  # Call to get the user's name
    greet_user(name)  # Call to greet the user
