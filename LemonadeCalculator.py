def greet_customer():
    print("Fresh lemonade made just for you")
    print("Welcome to my lemonade stand calculator")
greet_customer()
price=float(input("Price of each cup"))
cups=int(input("Number of cups bought today"))
def calculate_total(price,cups):
    total=price*cups
    return total
total=calculate_total(price,cups)
print("Total bill",calculate_total(price,cups),"$")
amount_paid=float(input("Amount paid"))
def calculator_change(amount_paid,total):
    change=amount_paid-total
    return change
print("Change",calculator_change(amount_paid,total))
if cups>=5:
    print("Wow thanks for big order")
else:
    print("Thanks for your support")
