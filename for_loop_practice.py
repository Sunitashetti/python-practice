# Loop over a list
cities = ["bengaluru", "mangaluru", "hubballi", "dharwad"]
for city in cities:
    print(city)

print("--------------")

# Loop over a string
name = "karnataka"
for letter in name:
    print(letter)

print("--------------")

# Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

print("--------------")

# Nested loop - multiplication table
for i in range(1, 9):
    for j in range(1, 9):
        print(f"{i} x {j} = {i*j}")
    print()
