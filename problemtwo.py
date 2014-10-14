import re
import sys

from basket import Basket
from category import Category, ExceptionCategory
from lineitem import LineItem
from tax import Tax


# last_minute_hack rearranges the lineitem description such that 'imported'
# appears at the beginning:
#   '1 box of imported chocolates at 11.25'
#   -> '1 imported box of chocolates: 11.85'
def last_minute_hack(tax_obj):
    def foo(lineitem):
        imported = u' imported'
        i = lineitem.description.find(imported)
        if i > -1:
            lineitem.description = imported[1:] + ' ' + \
                                   lineitem.description[:i] + \
                                   lineitem.description[i+len(imported):]
        return tax_obj.calculate(lineitem.value * lineitem.quantity)

    return foo


def parse_lineitem(lineitem_str):
    # Group 1: Quantity, 2: Description, 3: Price
    r = r'^(\d+(?:\.\d+)?) (.*) at (\d+(?:\.\d{1,2})?)$'
    m = re.match(r, lineitem_str)
    if m:
        return LineItem(m.group(1), m.group(2), m.group(3))
    return None


def main(argv):

    # Configure the application, including taxes and categories
    sales_tax_exceptions = []
    if len(argv) > 1:
        with open(argv[1]) as f:
            for line in f:
                sales_tax_exceptions.append(line.strip())

    sales_tax = Tax('0.10')
    import_duty = Tax('0.05')

    # Using the same name for both taxes ensures they're aggregated and
    # printed out on the same line
    categories = [
        ExceptionCategory(
            u'Sales Taxes',
            sales_tax_exceptions,
            lambda i: sales_tax.calculate(i.value * i.quantity)
        ),
        Category(
            u'Sales Taxes',
            [u'imported'],
            last_minute_hack(import_duty)
        ),
#        Category(
#            'Student Discount',
#            ['book'],
#            lambda i: (-1) * sales_tax.calculate(i.value * i.quantity)
#        )
    ]

    # Create a basket
    basket = Basket(categories)

    # Add line items
    with open(argv[0]) as f:
        for line in f:
            line_item = parse_lineitem(line.strip())
            if line_item:
                basket.add_line(line_item)

    # "Checkout"
    print basket.receipt()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print u'problemtwo.py <line items input file> <sales tax exceptions file>'
        sys.exit(1)
    main(sys.argv[1:])