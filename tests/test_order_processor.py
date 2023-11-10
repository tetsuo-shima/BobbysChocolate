import unittest
from enum import Enum

from order_processor import OrderProcessor


class TestOrderProcessor(unittest.TestCase):
    def test_create_order_sheet(self):
        class Flavors(Enum):
            apple = 1
            grape = 2
            cherry = 3

        expected = {'apple': 0, 'grape': 0, 'cherry': 0}

        self.assertEqual(OrderProcessor.create_order_sheet(Flavors), expected)


    def test_process_order_int(self):
        order = {'type': 'milk', 'cash': 12, 'price': 2, 'ratio': 5}
        expected = {'milk': 6, 'violet': 0, 'espresso': 0}
        self.assertEqual(OrderProcessor.process_order(order), expected)

    def test_process_order_int_bonus(self):
        order = {'type': 'milk', 'cash': 12, 'price': 2, 'ratio': 5}
        expected = {'milk': 7, 'violet': 0, 'espresso': 0}
        self.assertEqual(OrderProcessor.process_order(order, True),
                         expected)

    def test_process_order_float_bonus(self):
        order = {'type': 'violet', 'cash': 13.4, 'price': 4, 'ratio': 1}
        expected = {'milk': 0, 'violet': 6, 'espresso': 0}
        self.assertEqual(OrderProcessor.process_order(order, True),
                         expected)

    def test_process_order_float(self):
        order = {'type': 'milk', 'cash': 12.5, 'price': 2.0, 'ratio': 5.0}
        expected = {'milk': 6, 'violet': 0, 'espresso': 0}
        self.assertEqual(OrderProcessor.process_order(order), expected)

    def test_process_bonus_milk(self):
        order = {'type': 'milk', 'cash': 12.5, 'price': 2.0, 'ratio': 5.0}
        expected = 1
        self.assertEqual(OrderProcessor.process_bonus(order), expected)

    def test_process_bonus_violet(self):
        order = {'type': 'violet', 'cash': 13, 'price': 4, 'ratio': 1}
        expected = 3
        self.assertEqual(OrderProcessor.process_bonus(order), expected)




