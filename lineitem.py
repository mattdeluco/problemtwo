from decimal import Decimal


class LineItem(object):
    """
    LineItem represents an item in a basket and a line on a receipt.
    """

    def __init__(self, quantity, description, value):
        self.quantity = Decimal(quantity)
        self.description = description
        self.value = Decimal(value)
        self.categories = {}

    def total(self):
        """
        Calculate the total of this line item based on quantity and applied
        category functions.
        :return:
        """
        total = self.value * self.quantity
        for value in self.categories.itervalues():
            total += value
        return total

    def categorize(self, category):
        """
        Apply category to the lineitem and save the value returned from the
        category function.
        :param category:
        :return:
        """
        if category.name not in self.categories:
            self.categories[category.name] = 0
        self.categories[category.name] += category.fn(self)
