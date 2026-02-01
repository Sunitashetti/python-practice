debugging.py
# Debugging in Python

# Example 1: simple bug
a = 10
b = 0

try:
    result = a / b
    print(result)
except Exception as e:
    print("Error:", e)


# Example 2: logical debugging
numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total += num

print("Total:", total)


# Example 3: using print for debugging
x = 5
y = 10
z = x + y
print("x:", x)
print("y:", y)
print("z:", z)
