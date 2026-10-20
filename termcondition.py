def terms():
    ans = input("Accept terms and condition ? (yes/no): ")
    return ans

n = int(input("Enter number of user: "))

for i in range(n):
    print("User", i + 1 )   # i+1 to show user 1 otherwise It will be User 0
    option = terms()

    if option == "yes":
        print("Terms and condition accepted")
    elif option == "no":
        print("Terms and condition rejected")
    else:
        print("Invalid input")