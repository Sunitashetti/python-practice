# Tuples in Python

# Creating a tuple
genders = ("male", "female", "others")
print(genders)

# Accessing elements
print(genders[0])
print(genders[1])

# Length of tuple
print("Length:", len(genders))

# Loop through tuple
for gender in genders:
    print(gender)

# Tuples are immutable (cannot be changed)
# genders[0] = "boy"  # This will give an error
