# Day 18 - Dictionary and Loop Practice
# Topic: Dictionaries, For Loops, Filtering, Basic Logic

# 1. Total price of items from a dictionary
items = {
    "apple": 50,
    "banana": 30,
    "orange": 100
}

total_price = 0
for price in items.values():
    total_price += price

print("Total price of all items:", total_price)


# 2. Multiplication table using for loop
print("\nMultiplication Table (1 to 10):")
for num in range(1, 11):
    print(f"{num} x {num} = {num * num}")


# 3. Student data stored in dictionary
students = [
    {"name": "Ram", "age": 20, "marks": 50},
    {"name": "Charan", "age": 25, "marks": 45},
    {"name": "Bhim", "age": 22, "marks": 45}
]

print("\nStudent Details:")
for std in students:
    print("Name:", std["name"])
    print("Age:", std["age"])
    print("Marks:", std["marks"])
    print("-----")


# 4. Filter cities based on population
cities = {
    "Bengaluru": 10,
    "Belgaum": 8,
    "Mysore": 16
}

filtered_cities = {city: pop for city, pop in cities.items() if pop >= 10}

print(filtered_cities)
