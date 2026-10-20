num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Enter 1 for addition,2 for subtract,3 for divide,4 for multiply")
result = int(input())
if result == 1:
    print(num1 + num2)
elif result == 2:
    print(num1 - num2)
elif result == 3:
    print(num1 / num2)
else:
    print(num1 * num2)

