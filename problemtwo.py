import re
import sys

from lineitem import LineItem


class ProblemTwo(object):

    def __init__(self):
        pass


def parse_lineitem(lineitem_str):
    # Group 1: Quantity, 2: Description, 3: Price
    r = '^(\d+(?:\.\d+)?) (.*) at (\d+(?:\.\d{1,2})?)$'
    m = re.match(r, lineitem_str)
    return LineItem(m.group(1), m.group(2), m.group(3))


def main(argv):
    if len(argv) < 1:
        print 'problemtwo.py <line items input file> <sales tax exceptions file>'

    lineitems = []
    with open(argv[0]) as f:
        lineitems.append(parse_lineitem(f.readline()))


if __name__ == '__main__':
    main(sys.argv[1:])