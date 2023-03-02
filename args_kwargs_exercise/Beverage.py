from Food import Food


class Beverage(Food):
    """This class represents a beverage sold in a restaurant.
    The Beverage class inherits the attributes from its parent class Food, and has only additional attribute,
    which is size. Size must be 'small', 'medium' or 'large'.
    It also inherits the get_info function declared in its parent class Food."""

    def __init__(self, name, calories, price, size):
        super().__init__(name, calories, price)
        self.size = size
