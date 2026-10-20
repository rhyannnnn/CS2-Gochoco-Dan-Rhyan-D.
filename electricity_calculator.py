# Electricity Bill Calculator
RATE = 12.90
name = input("Enter customer name: ")
previous = float(input("Enter previous meter reading: "))
current = float(input("Enter current meter reading: "))

try:
    if name == "":
        print("Your name is: ", name)
    elif len(name) != 1:
        print("Enter your name")
except ValueError:
    print("Please don't leave your name blank")
try:
    previousint = int(previous)
    if 0 <= previousint:
        print("Previous reading is acceptable")
    else:
        print("Previous number must atleast be 0")
except ValueError:
    print("Must be a valid number")

try:
    currentint = int(current)
    if previousint <= currentint:
        print("Current reading is valid")
    else:
        print("Currrent reading must be more than previous reading")
except ValueError:
    print("Current reading must atleast be the previous reading")





consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading
