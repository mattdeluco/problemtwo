import decimal
import unittest

from lineitem import LineItem

class TestLineItem(unittest.TestCase):

    def test_basic(self):
        i = LineItem('1 book at 12.49')
        self.assertEqual(decimal.Decimal('1'), i.quantity)
        self.assertEqual(decimal.Decimal('12.49'), i.value)
        self.assertEqual('book', i.description)