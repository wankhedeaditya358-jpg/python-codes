family = []
n = int(input("Enter number of family members: "))
i = 0
while i < n:
    name = input("Enter member name: ")
    family.append(name)
    i = i + 1                         
print("Number of family member:",n)
# print("Family members :",family)    

for name in family:
    print(name)