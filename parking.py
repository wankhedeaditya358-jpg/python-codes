capacity = int(input("Enter the number of cars parked: "))

def slot1(capacity):
    if capacity > 50:
        print("Go to another parking slot")
    else:
        return print("Welcome to parking slot1")

slot1(capacity)