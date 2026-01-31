# Advanced loop concepts in Python

# Example 1: Nested for loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# Example 2: for loop with else
for num in range(1, 6):
    print(num)
else:
    print("Loop completed successfully")


# Example 3: pass statement
for i in range(5):
    if i == 3:
        pass  # placeholder
    print(i)


# Example 4: enumerate()
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(index, name)


# Example 5: zip()
numbers = [1, 2, 3]
letters = ["A", "B", "C"]

for n, l in zip(numbers, letters):
    print(n, l)
