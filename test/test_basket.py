from decimal import Decimal
import unittest

from basket import Basket
from category import Category, ExceptionCategory
from lineitem import LineItem
from tax import Tax


output1 = """1 book: 12.49
1 music CD: 16.49
1 chocolate bar: 0.85
Sales Taxes: 1.50
Total: 29.83
"""

output2 = """1 imported box of chocolates: 10.50
1 imported bottle of perfume: 54.65
Sales Taxes: 7.65
Total: 65.15
"""

output3 = """1 imported bottle of perfume: 32.19
1 bottle of perfume: 20.89
1 packet of headache pills: 9.75
1 imported box of chocolates: 11.85
Sales Taxes: 6.70
Total: 74.68
"""


class TestBasket(unittest.TestCase):

    def setUp(self):
        def last_minute_hack(lineitem):
            # '1 box of imported chocolates at 11.25'
            # -> '1 imported box of chocolates: 11.85'
            imported = ' imported'
            i = lineitem.description.find(imported)
            if i > -1:
                lineitem.description = imported[1:] + ' ' + \
                                       lineitem.description[:i] + \
                                       lineitem.description[i+len(imported):]
            return import_duty.calculate(lineitem.value * lineitem.quantity)

        categories = []

        sales_tax = Tax('0.10')
        sales_tax_categories = [
            'book', 'chocolate bar', 'chocolates', 'headache pills'
        ]
        categories.append(ExceptionCategory(
            'Sales Taxes',
            sales_tax_categories,
            lambda i: sales_tax.calculate(i.value * i.quantity)))

        import_duty = Tax('0.05')
        import_duty_categories = ['imported']
        categories.append(Category(
            'Sales Taxes',
            import_duty_categories,
            last_minute_hack))
            #lambda i: import_duty.calculate(i.value * i.quantity)))

        self.categories = categories

    def test_input1(self):
        lineitems = [
            '1 book at 12.49',
            '1 music CD at 14.99',
            '1 chocolate bar at 0.85'
        ]

        basket = Basket(self.categories)
        for line in lineitems:
            basket.add_line(LineItem(line))

        self.assertEqual(Decimal('29.83'), basket.total())
        self.assertEqual(output1, basket.receipt())

    def test_input2(self):
        lineitems = [
            '1 imported box of chocolates at 10.00',
            '1 imported bottle of perfume at 47.50'
        ]
        basket = Basket(self.categories)
        for line in lineitems:
            basket.add_line(LineItem(line))

        self.assertEqual(Decimal('65.15'), basket.total())
        self.assertEqual(output2, basket.receipt())

    def test_input3(self):
        lineitems = [
            '1 imported bottle of perfume at 27.99',
            '1 bottle of perfume at 18.99',
            '1 packet of headache pills at 9.75',
            '1 box of imported chocolates at 11.25'
        ]

        basket = Basket(self.categories)
        for line in lineitems:
            basket.add_line(LineItem(line))

        self.assertEqual(Decimal('74.68'), basket.total())
        self.assertEqual(output3, basket.receipt())

