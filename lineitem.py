from decimal import Decimal


class LineItem(object):

    def __init__(self, quantity, description, value):
        self.quantity = Decimal(quantity)
        self.description = description
        self.value = Decimal(value)
        self.categories = {}

    def total(self):
        total = self.value * self.quantity
        for value in self.categories.itervalues():
            total += value
        return total

    def categorize(self, category):
        if category.name not in self.categories:
            self.categories[category.name] = 0
        self.categories[category.name] += category.fn(self)
