from decimal import Decimal
import unittest

import tax


class TestTax(unittest.TestCase):

    def setUp(self):
        self.import_duty = tax.Tax('0.05')
        self.sales_tax = tax.Tax('0.10')

    def test_calculate(self):
        self.assertEqual(Decimal('0.05'), self.import_duty.calculate('1'))

    def test_quantum(self):
        self.assertTrue(
            self.sales_tax.calculate('14.99').same_quantum(Decimal('1.00')))

    def test_input1(self):
        book = Decimal('12.49')
        music_cd = Decimal('14.99')
        chocolate_bar = Decimal('0.85')
        taxes = self.sales_tax.calculate(music_cd)

        total = book + music_cd + chocolate_bar + taxes
        self.assertEqual(Decimal('29.83'), total)

    def test_input2(self):
        line1 = Decimal('10.00') + self.import_duty.calculate('10.00')
        line2 = Decimal('47.50') \
                + self.import_duty.calculate('47.50') \
                + self.sales_tax.calculate('47.50')

        receipt = line1 + line2
        self.assertEqual(Decimal('65.15'), receipt)

    def test_input3(self):
        imported_parfum = Decimal('27.99')
        parfum = Decimal('18.99')
        pills = Decimal('9.75')
        imported_chocolate = Decimal('11.25')

        taxes = 0
        for t in [imported_parfum, imported_chocolate]:
            taxes += self.import_duty.calculate(t)
        for t in [imported_parfum, parfum]:
            taxes += self.sales_tax.calculate(t)

        total = imported_parfum + parfum + pills + imported_chocolate + taxes
        self.assertEqual(Decimal('74.68'), total)
