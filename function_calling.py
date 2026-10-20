def caculate_gst(category,price):
    if category == "food":
        gst = 5
    elif category == "electronics":
        gst = 18
    elif category == "recycled":
        gst = 5 
    else:
        gst = 0
    return price * gst / 100

def order_total():
    n = int(input("Enter number of products purchased: "))
    total = 0

    for i in range(n):
        print("\nProducts",i + 1)
        name = input("Enter product name: ")
        category = input("Enter category(food/electronics/recycled): ")
        price = float(input("Enter product price: "))

        gst = caculate_gst(category,price)
        final_price = price + gst
        total = total + final_price
        print("Product:",name)
        print("Price with GST:",final_price)

        print("Total number of products:",name)
        print("Total bill including GST:",total)

order_total()