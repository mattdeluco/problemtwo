from decimal import Decimal
import unittest

from basket import Basket
from category import Category, ExceptionCategory
from problemtwo import parse_lineitem, last_minute_hack
from tax import Tax


output1 = u"""1 book: 12.49
1 music CD: 16.49
1 chocolate bar: 0.85
Sales Taxes: 1.50
Total: 29.83"""

output2 = u"""1 imported box of chocolates: 10.50
1 imported bottle of perfume: 54.65
Sales Taxes: 7.65
Total: 65.15"""

output3 = u"""1 imported bottle of perfume: 32.19
1 bottle of perfume: 20.89
1 packet of headache pills: 9.75
1 imported box of chocolates: 11.85
Sales Taxes: 6.70
Total: 74.68"""

output_no_input = u"""Sales Taxes: 0.00
Total: 0.00"""

output_one_item_exempt = u"""1 book: 10.00
Sales Taxes: 0.00
Total: 10.00
"""

class TestBasket(unittest.TestCase):

    def setUp(self):
        categories = []

        sales_tax = Tax('0.10')
        sales_tax_categories = [
            u'book', u'chocolate bar', u'chocolates', u'headache pills'
        ]
        categories.append(ExceptionCategory(
            'Sales Taxes',
            sales_tax_categories,
            lambda i: sales_tax.calculate(i.value * i.quantity)))

        import_duty = Tax('0.05')
        import_duty_categories = [u'imported']
        categories.append(Category(
            u'Sales Taxes',
            import_duty_categories,
            last_minute_hack(import_duty)))

        self.categories = categories

    def test_input1(self):
        lineitems = [
            u'1 book at 12.49',
            u'1 music CD at 14.99',
            u'1 chocolate bar at 0.85'
        ]

        basket = Basket(self.categories)
        for line in lineitems:
            basket.add_line(parse_lineitem(line))

        self.assertEqual(Decimal('29.83'), basket.total())
        self.assertEqual(output1, basket.receipt())

    def test_input2(self):
        lineitems = [
            u'1 imported box of chocolates at 10.00',
            u'1 imported bottle of perfume at 47.50'
        ]
        basket = Basket(self.categories)
        for line in lineitems:
            basket.add_line(parse_lineitem(line))

        self.assertEqual(Decimal('65.15'), basket.total())
        self.assertEqual(output2, basket.receipt())

    def test_input3(self):
        lineitems = [
            u'1 imported bottle of perfume at 27.99',
            u'1 bottle of perfume at 18.99',
            u'1 packet of headache pills at 9.75',
            u'1 box of imported chocolates at 11.25'
        ]

        basket = Basket(self.categories)
        for line in lineitems:
            basket.add_line(parse_lineitem(line))

        self.assertEqual(Decimal('74.68'), basket.total())
        self.assertEqual(output3, basket.receipt())

    def test_input3_2(self):
        lineitems = [
            u'1 imported bottle of perfume at 27.99',
            u'1 bottle of perfume at 18.99',
            u'1 packet of headache pills at 9.75',
            u'1 box of imported chocolates at 11.25'
        ]

        basket = Basket(self.categories)
        for line in lineitems:
            basket.add_line(parse_lineitem(line))

        self.assertEqual(output3, basket.receipt())

    def test_poor_input(self):
        lineitems = [
            u'1 imported bottle of perfume at 27.99',
            u'1 bottle of perfume at 18.99',
            u'1 packet of headache pills at 9.75',
            u'1 box of imported chocolates at 11.25',
            u'abc123 blah blah'
        ]

        basket = Basket(self.categories)
        for line in lineitems:
            line_item = parse_lineitem(line)
            if line_item:
                basket.add_line(line_item)

        self.assertEqual(output3, basket.receipt())

    @unittest.skip('Unresolved corner-case.')
    def test_no_input(self):
        basket = Basket(self.categories)
        self.assertEqual(output_no_input, basket.receipt())

    @unittest.skip('Unresolved corner-case.')
    def test_one_item_exempt(self):
        lineitems = [
            u'1 book at 10.00'
        ]

        basket = Basket(self.categories)
        for line in lineitems:
            line_item = parse_lineitem(line)
            if line_item:
                basket.add_line(line_item)

        self.assertEqual(output_one_item_exempt, basket.receipt())