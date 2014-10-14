from decimal import Decimal


class LineItem(object):

    def __init__(self, quantity, description, value):
        self.quantity = Decimal(quantity)
        self.description = description
        self.value = Decimal(value)
        self.categories = []

    def itemized_categories(self):
        items = {}
        for c in self.categories:
            if c.name not in items:
                items[c.name] = 0
            items[c.name] += c.fn(self)
        return items

    def total(self):
        items = self.itemized_categories()
        total = self.value * self.quantity
        for i in items.itervalues():
            total += i
        return total

    def categorize(self, category):
        self.categories.append(category)
