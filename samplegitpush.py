# 1. Defining a Function
def greet_user(username):
    """This function greets the user by their name."""
    print(f"\nHello, {username}! Welcome to Python.")


# 2. Variables and Basic Output
title = "Python Basics Demo"
print(f"--- {title} ---")

# 3. User Input
name = input("Enter your name: ")

# 4. Function Call
greet_user(name)

# 5. Conditional Logic (if-elif-else)
try:
    age = int(input("Enter your age: "))

    if age < 0:
        print("Age cannot be negative.")
    elif age < 18:
        print("You are a minor.")
    else:
        print("You are an adult.")
except ValueError:
    print("Please enter a valid number for age.")

# 6. Loops and Lists
print("\nCounting down from 3 using a list and loop:")
countdown_items = [3, 2, 1]

for item in countdown_items:
    print(f"Time left: {item}...")

print("Blast off! ")