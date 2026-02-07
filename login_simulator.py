username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
elif username == "admin":
    print("Wrong password")
else:
    print("User not found")
