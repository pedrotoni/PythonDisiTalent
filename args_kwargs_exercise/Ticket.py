import math


class Ticket:
    """The Ticket class represents a restaurant ticket. When instatiating a Ticket object, you should insert
    two parameters:
    *items_consumed -> the parameters in the constructor should be Food/Beverage objects.
     the '*' simbolizes that the number of parameters accepted is non-especified, and these parameters are
     non-keyword arguments as well.
     **restaurant_info -> the restaurant_info parameter must be in dictionary form.
     the '**' simbolizes that the number of parameters accepted is non-especified, and these parameters are
     keyword arguments.
     """

    def __init__(self, *items_consumed, **restaurant_info):
        self.items_consumed = items_consumed
        self.restaurant_info = restaurant_info

    def sum_total(self):
        """
        This function sums all the prices of items consumed and returns us the total value of the bill.
        The sum_total function works with a variable 'total' starting in 0.
        As we iterate through the list of consumed items, we sum the price of each consumed item
        to the total, returning the total value at the end of the execution.
        """
        total = 0
        for item in self.items_consumed:
            total += item.price
        return total

    def price_per_person(self, number_of_people):
        """
        The price_per_person gives us the price each person must pay, after dividing the total value of the bill
        by the number of people in the table.
        the number_of_people parameter must be an integer.
        In this function we have a 'variable' as well, but in this case, the 'total' receives the return
        of the sum_total function. Then we divide this total by the integer passed as the number_of_people
        parameter, and upper round it with the math.ceil function.
        After all we return a message saying that the bill was splitted by the number of people at the table,
        and how much each person must pay.
        """
        total = self.sum_total()
        price_per_person = math.ceil(total / number_of_people)
        return f"The bill was splitted by {number_of_people}.\n" \
               f"Price per person: ${price_per_person:.2f}"

    def print_ticket(self):
        """
        The print_ticket function prints the restaurant info and the bill info for a ticket.
        For the restaurant info, we iterate through the restaurant info dictionary (self.restaurant_info.items()),
        and concatenate the keys and values to a initial empty string stored in the restaurant_info variable.
        We do a similar process for the bill_info, but in this case, we iterate through the consumed items list
        (self.items_consumed), and we concatenate each consumed item name and price to a initial empty string
        stored in the bill_info variable.
        """
        print("--------------------")
        print("Here is your ticket: ")
        total = self.sum_total()
        restaurant_info = ""
        bill_info = ""
        for key, value in self.restaurant_info.items():
            restaurant_info += f"{key} - {value}\n"
        print(restaurant_info)

        for item in self.items_consumed:
            bill_info += f"{item.name} - ${item.price:.2f}\n"
        print(bill_info)
        print(f"Total: ${total:.2f}")
