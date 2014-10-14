

class Category(object):

    def __init__(self, name, descriptions=None, fn=lambda lineitem: 0):
        """
        Create a category to which fn() is applied for matching descriptions.

        :param name:
        :param descriptions: A list of strings to
        :param fn: A function with parameters value and quantity
        :return:
        """
        self.name = name
        self.descriptions = descriptions or []
        self.fn = fn

    def categorize(self, lineitem):
        for desc in self.descriptions:
            if desc in lineitem.description:
                lineitem.categorize(self)



class ExceptionCategory(Category):

    def __init__(self, *args, **kwargs):
        super(ExceptionCategory, self).__init__(*args, **kwargs)

    def categorize(self, lineitem):
        for desc in self.descriptions:
            if desc in lineitem.description:
                return
        lineitem.categorize(self)
