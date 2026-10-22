name=input("enter student name :")
roll_no=int(input("enter roll no.:"))
age = int(input("enter age :"))

maths=float(input("enter maths marks :"))
science=float(input("enter science marks :"))
english=float(input("enter english marks :"))

total_marks=maths + science + english 
average_marks= total_marks/3
percentage=(total_marks/300)*100

print("\n-------------------report card------------------")
print(f"name : {name}")
print(f"roll no. : {roll_no}")
print(f"age : {age}")
print(f"maths :{maths}")
print(f"science :{science}")
print(f"english :{english}")
print(f"total :{total_marks}")
print(f"average :{average_marks}")
print(f"percentage :{percentage}%")