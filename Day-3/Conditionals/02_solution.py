day = (input("Today day:- "))
age = int(input("Enter age:- "))
price = int(input("Enter price:- "))

if day == "Wednesday":
    price -= 2

if age < 18:
    price -= 8
elif age >= 18:
    price -= 12

print("Ticket price for you is $", price)