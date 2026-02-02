# Practice problems using if, else, elif and debugging

# Problem 1: Check grade

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# Problem 2: Check largest of three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Largest:", a)
elif b > a and b > c:
    print("Largest:", b)
else:
    print("Largest:", c)


# Problem 3: Debugging example

x = int(input("Enter a number: "))

if x % 2 == 0:
    print("Even number")
else:
    print("Odd number")
