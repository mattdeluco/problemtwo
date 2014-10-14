import decimal
import re


class LineItem(object):

    # TODO: Abstract line parsing out of LineItem
    def __init__(self, line, r='^(\d+(?:\.\d+)?) (.*) at (\d+(?:\.\d{1,2})?)$'):
        m = re.match(r, line)
        self.quantity = decimal.Decimal(m.group(1))
        self.description = m.group(2)
        self.value = decimal.Decimal(m.group(3))
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
