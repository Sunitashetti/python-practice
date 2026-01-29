# While loop in Python

# Example 1: simple while loop
i = 1
while i <= 5:
    print(i)
    i += 1


# Example 2: using break
number = 1
while number <= 10:
    if number == 6:
        break
    print(number)
    number += 1


# Example 3: using continue
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print("Odd number:", num)


# Example 4: nested while loop
row = 1
while row <= 3:
    col = 1
    while col <= 3:
        print("*", end=" ")
        col += 1
    print()
    row += 1
