roll_No = [139,155,170,185,199,204]
find = False
search = int(input("Enter the roll number to check whether its present or not: "))

for i in range(len(roll_No)):
    if search == roll_No[i]:
        find = True
        break   #if student is presnt stop the loop

if find == True:
    print("Student is Present")
else:
    print("Student is absent")