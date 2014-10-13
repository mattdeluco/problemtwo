import unittest

from category import Category, ExceptionCategory


class MockItem(object):
    def __init__(self, description):
        self.description = description
        self.called = False

    def categorize(self, category):
        self.called = True


class TestCategory(unittest.TestCase):

    def test_basic(self):
        name = 'music'
        c = Category(name)

        self.assertEqual(name, c.name)
        self.assertEqual(0, len(c.descriptions))
        self.assertEqual(0, c.fn(1, 2))

    def test_categorize(self):
        cat = Category('Discount', ['foo', 'bar', 'baz'])
        item = MockItem('foo')
        cat.categorize(item)
        self.assertTrue(item.called)

    def test_not_categorize(self):
        cat = Category('Discount', ['foo', 'bar', 'baz'])
        item = MockItem('quux')
        cat.categorize(item)
        self.assertFalse(item.called)


class TestExceptionCategory(unittest.TestCase):

    def test_exceptional_item(self):
        cat = ExceptionCategory('Discount', ['foo', 'bar', 'baz'])
        item = MockItem('foo')
        cat.categorize(item)
        self.assertFalse(item.called)

    def test_not_exceptional_item(self):
        cat = ExceptionCategory('Discount', ['foo', 'bar', 'baz'])
        item = MockItem('quux')
        cat.categorize(item)
        self.assertTrue(item.called)
