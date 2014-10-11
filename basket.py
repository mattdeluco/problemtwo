import decimal
from tax import SalesTax

class Basket(object):

    def __init__(self, context):
        context = context or decimal.BasicContext.copy()
        context.prec = 2
        context.rounding = decimal.ROUND_HALF_UP
        self.context = context

        self.line_items = []

    def add(self, line_item):
        # Apply rules to line item
        self.line_items.append(line_item)

    def print_receipt(self):
        pass