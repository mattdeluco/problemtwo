
class Money(object):

    def __init__(self, value):
        try:
            value = int(value)
        except ValueError:
            value = float(value)
        self.value = int(value * 100)

    def add(self, value):
        pass

    def subtract(self, value):
        return self.add(-1 * value)

    def multiply(self, value):
        pass

    def divide(self, value):
        pass
