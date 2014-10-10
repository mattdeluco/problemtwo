import decimal

class Tax(object):
    def __init__(self, rate):
        self.rate = decimal.Decimal(rate)

    def calculate(self, amount):
        return decimal.Decimal(amount) * self.rate


class SalesTax(Tax):
    def __init__(self, exceptions, **kwargs):
        super(SalesTax, self).__init__(**kwargs)
        self.exceptions = set(exceptions)

    def calculate(self, category, **kwargs):
        if category not in self.exceptions:
            return super(SalesTax, self).calculate(**kwargs)
        return 0
