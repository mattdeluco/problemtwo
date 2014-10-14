

class Basket(object):
    """
    :type lineitems: list[LineItem]
    """

    def __init__(self, categories):
        """
        Create a new shopping basket associated with the given categories.
        :type categories: list[Category]
        :param categories: Categories to be applied to lineitems
        :return:
        """
        self.categories = categories
        self.lineitems = []

    def add_line(self, lineitem):
        """
        Categorize and add a lineitem to this basket.
        :type lineitem: LineItem
        :param lineitem:
        :return:
        """
        for c in self.categories:
            c.categorize(lineitem)
        self.lineitems.append(lineitem)

    def total(self):
        """
        Return the total (not subtotal) of this basket.
        :return:
        """
        total = 0
        for line in self.lineitems:
            total += line.total()
        return total

    def receipt(self):
        """
        Return an itemized receipt for this basket.
        :return: list
        """
        receipt = ''
        itemized_cats = {}

        for line in self.lineitems:
            receipt += "{qty} {desc}: {total}\n".format(
                qty=line.quantity,
                desc=line.description,
                total=line.total())

            for key, value in line.itemized_categories().iteritems():
                if key not in itemized_cats:
                    itemized_cats[key] = 0
                itemized_cats[key] += value

        for key, value in itemized_cats.iteritems():
            receipt += "{desc}: {value}\n".format(desc=key, value=value)

        receipt += "Total: {}".format(self.total())

        return receipt