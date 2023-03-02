from Ticket import Ticket
from Food import Food
from Beverage import Beverage

# implementation

burger = Food("burger", 1000, 30.00)
coke = Beverage("coke", 600, 13.00, "Large")
fanta = Beverage("fanta", 500, 8.00, "Small")
fries = Food("fries", 300, 10.00)
pie = Food("pie", 300, 32.00)
salad = Food("salad", 100, 25.00)
juice = Beverage("juice", 300, 5.50, "Small")
coffee = Beverage("coffee", 350, 11.20, "Small")
beer = Beverage("beer", 400, 15.00, "Medium")
soup = Food("soup", 300, 22.35)

# print_ticket() and price_per_person functions
ticket1 = Ticket(burger, coke, fries, pie, fanta, restaurant="Python Burger", branch="São Paulo", waiter="Maria")
ticket1.print_ticket()
print(ticket1.price_per_person(3))

ticket2 = Ticket(salad, juice, soup, pie, beer, restaurant="Python Cafe",
                 branch="Rio de Janeiro", waiter="Marcelo", culinary="vegetarian", parking_fee=5.00)
ticket2.print_ticket()
print(ticket2.price_per_person(2))
print("")

# get_info function using object.__dict__ (Food and Beverage classes)
# Beverage
beer_info = beer.get_info()
for key, value in beer_info.items():
    print(f"{key} - {value}")
print("-------------------")

# Food
soup_info = soup.get_info()
for key, value in soup_info.items():
    print(f"{key} - {value}")
print("-------------------")
