n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))  

count = 0
i = n1 + 1                      # i=n+1 coz we are considering number bet n1 and n2 not n1

while i < n2:
    if i % 2 != 0:
        count = count + i
    i = i + 1                #increment i otherwise loop run forever

print("Sum of odd between numbers:",count)