class Food:
    """
    The Food class represents some food sold in a restaurant.
    It has the following attributes:
    name -> should be a string
    calories -> should be a integer
    price -> should be a float number
    This class also has a daughter class called beverage, which inherits the Food class attributes and get_info method.
    """
    def __init__(self, name, calories, price):
        self.name = name
        self.calories = calories
        self.price = price

    def get_info(self):
        """
        This method returns the information of the food in form of a dictionary.
        """
        return self.__dict__
