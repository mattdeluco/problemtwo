

class Category(object):
    """
    Category is uesd to categorize lineitems and optionally apply a function
    to the lineitem to perform actions such as calculating taxes or discounts.
    """

    def __init__(self, name, descriptions=None, fn=lambda lineitem: 0):
        """
        Create a category to which fn() is applied for matching descriptions.

        :param name: The category name
        :param descriptions: A list of strings against which a lineitem
        description is matched
        :param fn: A function that takes a lineitem as its only argument
        :return:
        """
        self.name = name
        self.descriptions = descriptions or []
        self.fn = fn

    def categorize(self, lineitem):
        """
        Apply this category to the lineitem if its description matches.

        :param lineitem:
        """

        for desc in self.descriptions:
            if desc in lineitem.description:
                lineitem.categorize(self)



class ExceptionCategory(Category):
    """
    ExceptionCategory will not apply fn to the lineitem if any of its
    descriptions match the lineitem description.
    """

    def __init__(self, *args, **kwargs):
        super(ExceptionCategory, self).__init__(*args, **kwargs)

    def categorize(self, lineitem):
        for desc in self.descriptions:
            if desc in lineitem.description:
                return
        lineitem.categorize(self)
