from decimal import Decimal, ROUND_UP

class Tax(object):
    def __init__(self, rate):
        self.rate = Decimal(rate)

    def calculate(self, amount):
        twenty = Decimal('20')
        tax_amount = Decimal(amount) * self.rate
        tax_amount = (tax_amount * twenty).quantize(Decimal('1'),
                                                    rounding=ROUND_UP)
        return tax_amount / twenty


class SalesTax(Tax):
    def __init__(self, exceptions, **kwargs):
        super(SalesTax, self).__init__(**kwargs)
        self.exceptions = set(exceptions)

    def calculate(self, category, **kwargs):
        if category not in self.exceptions:
            return super(SalesTax, self).calculate(**kwargs)
        return 0
