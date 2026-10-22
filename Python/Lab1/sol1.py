# Student Fee Calculator

print("=" * 50)
print("          STUDENT FEE CALCULATOR")
print("=" * 50)

# Take fee details from student
t = int(input("Enter Tuition Fee: Rs "))
l = int(input("Enter Lab Fee: Rs "))
lib = int(input("Enter Library Fee: Rs "))
e = int(input("Enter Exam Fee: Rs "))
d = int(input("Enter Discount Amount: Rs "))

# Calculate total and final fee
total = t + l + lib + e
final = total - d

# Calculate annual and monthly fee
annual = final * 2
monthly = annual // 12

# Display calculations
print("\n--- Calculations ---")
print("Total Fee (before discount): Rs", total)
print("Final Fee (after discount): Rs", final)
print("Annual Fee (2 semesters): Rs", annual)
print("Monthly Installment: Rs", monthly)

# Display fee summary
print("\n" + "=" * 50)
print("             FEE SUMMARY")
print("=" * 50)

print("Tuition Fee       : Rs", t)
print("Lab Fee           : Rs", l)
print("Library Fee       : Rs", lib)
print("Exam Fee          : Rs", e)
print("Total Fee         : Rs", total)
print("Discount          : Rs", d)
print("Final Fee         : Rs", final)
print("Annual Fee        : Rs", annual)
print("Monthly Payment   : Rs", monthly)

print("=" * 50)