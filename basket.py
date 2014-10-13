

class Basket(object):

    def __init__(self, categories):
        """
        Create a new shopping basket associated with the given categories.
        :type categories: list[Category]
        :return:
        """
        self.categories = categories
        self.lineitems = []

    def add_line(self, lineitem):
        """
        Categorize and add a lineitem to this basket.
        :param lineitem:
        :return:
        """
        for c in self.categories:
            c.categorize(lineitem)
        self.lineitems.append(lineitem)

    def print_receipt(self):
        """
        Print an itemized receipt for this basket.
        :return:
        """
        pass
