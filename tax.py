import decimal

class Tax(object):
    def __init__(self, rate):
        self.rate = rate

    def calculate(self, amount):
        return amount * 100 / self.rate


class SalesTax(Tax):
    def __init__(self, exceptions, **kwargs):
        super(SalesTax, self).__init__(**kwargs)
        self.exceptions = exceptions

    def calculate(self, category, **kwargs):
        if category not in self.exceptions:
            return super(SalesTax, self).calculate(**kwargs)
