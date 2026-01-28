# Conditional statements in Python

number = int(input("Enter a number: "))

if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number")


# Example: check age
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
