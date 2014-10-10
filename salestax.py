
class SalesTax(object):
    def __init__(self, tax):
        self.tax = tax

    def calculate(self, amount):
        tax = amount*100 / self.tax