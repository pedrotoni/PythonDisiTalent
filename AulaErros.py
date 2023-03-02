# Exercise 1
# path = "C:/Users/M2M/PycharmProjects/disi/Basic.txt"
# try:
#     with open(path, "r") as file:
#         txt = file.read()
#         print(txt)
# except FileNotFoundError:
#     print("The file you're searching for does not exist.")

# Exercise 2
# class ListLengthError(Exception):
#     pass
#
# num_list = []
# print("Type '999' to exit.")
# while True:
#     try:
#         entry = int(input("Insert a number: "))
#         num_list.append(entry)
#         if entry == 999:
#             num_list.pop()
#             break
#     except ValueError:
#         print("Not a valid value.")
#
# if len(num_list) < 3:
#     raise ListLengthError("The list is not long enough. Try again.")
# else:
#     print(num_list)
#     print(f"The third element of the list {num_list} is {num_list[2]}.")

# Exercise 3
class ExistingItemError(Exception):
    pass

class UnexistingItemError(Exception):
    pass

class InsufficientInventoryError(Exception):
    pass

class Shop:

    def __init__(self, name, cif, address):
        self.name = name
        self.cif = cif
        self.address = address
        self.inventory = {}

    def add_item(self, item, amount):
        if item.lower() not in self.inventory.keys():
            self.inventory[item] = amount
        else:
            raise ExistingItemError(f"Could not add {item} on the list because its already in it.")



    def buy(self):
        item_buy = input("Which item you want to buy? ")
        if not item_buy.isalpha():
            raise TypeError("Item should be a word! Not numbers or special characters!")

        try:
            amount_buy = int(input("How many of this item you want to buy? "))
        except ValueError:
            raise TypeError("Amount should be a number!")

        if item_buy.lower() not in self.inventory.keys():
            raise UnexistingItemError(f"The item {item_buy} is not available in our shop.")
        elif amount_buy > self.inventory[item_buy.lower()]:
            raise InsufficientInventoryError(f"We don't have {amount_buy} amounts of {item_buy} available right now. Sorry.")
        else:
            print(f"You bought {amount_buy} {item_buy}.")

shop = Shop("Loja","20202020202","Rua 1")
shop.add_item("socks",100)
shop.add_item("shoe",50)
shop.add_item("shirt",30)
shop.add_item("pants",80)
shop.add_item("belt",120)

print("Inventory:")
for item, amount in shop.inventory.items():
    print(f"{item} - {amount}")
print("")

try:
    shop.add_item("SOCKS",10)
except ExistingItemError as e:
    print(e)

try:
    shop.buy()
except (UnexistingItemError, InsufficientInventoryError, TypeError) as e:
    print(e)







