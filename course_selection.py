Mca = 1
Mba = 2

course_number = int(input("Enter selected Course: "))
for i in range(2):
    for j in range(i):
        if course_number == 1:
            print("8 subjects in a semester")
        elif course_number == 2:
            print("10 subjects in a semester")
        else:
            print("You have entered wrong number")