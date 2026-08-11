def greet_customer():
    print("Hi welcome to my art supply store")
    print("Get creative right now with new deals on art supplies!")
greet_customer()
def calculate_total(price,supplies):
    total=price*supplies
    return total
price=float(input("Price of each supply"))
supplies=int(input("Number of supplies bought today"))
total=calculate_total(price,supplies)
print("Total bill",calculate_total(price,supplies),"$")
amount_paid=float(input("Amount paid"))
def calculator_change(amount_paid,total):
    change=amount_paid-total
    return change
print("Change",calculator_change(amount_paid,total))
if supplies>=5:
    print("Wow thanks for big order")
else:
    print("Thanks for your support")

