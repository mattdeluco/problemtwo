

class Category(object):

    def __init__(self, name, descriptions, fn=lambda val, qty: 0):
        self.name = name
        self.descriptions = descriptions or []
        self.fn = fn

    def categorize(self, lineitem):
        if lineitem.description in self.descriptions:
            lineitem.categorize(self)


class ExceptionCategory(Category):

    def __init__(self, *args, **kwargs):
        super(ExceptionCategory, self).__init__(*args, **kwargs)

    def categorize(self, lineitem):
        if lineitem.description not in self.descriptions:
            super(ExceptionCategory, self).categorize(lineitem)