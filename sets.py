# Sets in Python

# Creating a set
numbers = {1, 2, 3, 4, 5}
print(numbers)

# Adding elements
numbers.add(6)
print(numbers)

# Removing elements
numbers.remove(3)
print(numbers)

# Another set
even_numbers = {2, 4, 6, 8}

# Set operations
print("Union:", numbers.union(even_numbers))
print("Intersection:", numbers.intersection(even_numbers))
print("Difference:", numbers.difference(even_numbers))
