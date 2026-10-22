# Collect the visitor's basic information.
print("\nWelcome to the Theme Park System!\n")
name = input("Please enter your name: ")
birthyear = int(input("Please enter your birth year: "))
height = float(input("Please enter your height in centimeters: "))
vip = bool(int(input("Are you a VIP member? 1 for yes, 0 for no: ")))

# Convert measurements and calculate the visitor's eligibility.
age = 2026 - birthyear
height_meters = height / 100
can_ride = age >= 12 and height_meters >= 1.2
need_child_pass = age < 12 or height_meters < 1.4
need_adult_pass = age >= 18 and height_meters >= 1.4
can_ride_water_slide = height_meters >= 1.5
get_vip_access = vip and can_ride

# Display the visitor's information and access decisions.
print("\n--- Visitor Information ---")
print(f"Hello {name}!")
print(f"Your age is: {age} years old.")
print(f"Your height is: {height_meters:.2f} meters.")
print(f"VIP Member: {vip}")
print("\n--- Ride Eligibility ---")
print(f"Can Enter Park: {can_ride}")
print(f"Need child pass: {need_child_pass}")
print(f"Need adult pass: {need_adult_pass}")
print(f"Can ride water slide: {can_ride_water_slide}")
print(f"VIP access granted: {get_vip_access}")