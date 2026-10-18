name = input("Enter a String: ")

count = 0 
for i in name:
    if i == " ":
        count = count + 1
    
print("Number of Spaces:",count)