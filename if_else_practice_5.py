# Problem 11: Check password strength

password = input("Enter a password: ")

if len(password) >= 8:
    print("Strong password")
else:
    print("Weak password")


# Problem 12: Check even or odd using if-else

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# Problem 13: Temperature check

temp = float(input("Enter temperature: "))

if temp > 30:
    print("Hot weather")
elif temp >= 20:
    print("Normal weather")
else:
    print("Cold weather")
