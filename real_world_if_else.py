# Ticket Checker

age = int(input("Enter your age: "))

if age < 5:
    print("Free ticket")
elif age <= 18:
    print("Child ticket")
else:
    print("Adult ticket")


# Meal Time Checker

time = int(input("Enter time in 24-hour format: "))

if 6 <= time < 11:
    print("Breakfast time")
elif 11 <= time < 16:
    print("Lunch time")
elif 16 <= time < 20:
    print("Snacks time")
elif 20 <= time <= 23:
    print("Dinner time")
else:
    print("Invalid time")


# Traffic Signal

signal = input("Enter traffic signal color: ").lower()

if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Get Ready")
elif signal == "green":
    print("Go")
else:
    print("Invalid signal")
