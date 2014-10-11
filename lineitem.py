import re
import decimal

class LineItem(object):

    def __init__(self, line, r='^(\d+(?:\.\d+)?) (.*) at (\d+(?:\.\d{1,2})?)$'):
        m = re.match(r, line)
        self.quantity = decimal.Decimal(m.group(1))
        self.description = m.group(2)
        self.value = decimal.Decimal(m.group(3))
