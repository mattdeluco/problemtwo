from decimal import Decimal, ROUND_UP


class Tax(object):
    def __init__(self, rate):
        """
        Instantiate a Tax object with the given rate.
        :param rate: The tax rate associated with this Tax object
        :return:
        """
        self.rate = Decimal(rate)

    def calculate(self, amount):
        """
        Tax the given amount.
        Tax calculations are rounded up to the nearest 0.05.
        :param amount: The amount to tax
        :return: The amount of tax
        """
        twenty = Decimal('20')
        tax_amount = Decimal(amount) * self.rate
        tax_amount = (tax_amount * twenty).quantize(Decimal('1'),
                                                    rounding=ROUND_UP)
        return tax_amount / twenty
