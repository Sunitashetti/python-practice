# Dictionaries in Python

# Creating a dictionary
student = {
    "name": "John",
    "age": 20,
    "course": "Python"
}

print(student)

# Accessing values
print(student["name"])
print(student.get("age"))

# Updating values
student["age"] = 21
print(student)

# Adding new key-value pair
student["city"] = "Bangalore"
print(student)

# Removing elements
student.pop("course")
print(student)

# Dictionary methods
print(student.keys())
print(student.values())
print(student.items())

# Looping through dictionary
for key, value in student.items():
    print(key, ":", value)

# Built-in functions
print("Length:", len(student))
