import decimal
import unittest

import tax


class TestTax(unittest.TestCase):

    def test_calculate(self):
        import_duty = tax.Tax('0.05')

        self.assertEqual(decimal.Decimal('0.05'), import_duty.calculate('1'))


class TestSalesTax(unittest.TestCase):
    pass