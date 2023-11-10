import unittest
from collections import OrderedDict
from enum import Enum

from order_processor import ChocolateType, OrderProcessor


class TestOrderProcessor(unittest.TestCase):
    def test_process_order_int(self):
        order = {'type': 'milk', 'cash': 12, 'price': 2, 'ratio': 5}
        expected = {'milk': 6, 'violet': 0, 'espresso': 0}
        self.assertEqual(OrderProcessor.process_order(order), expected)

    def test_prcess_order_float(self):
        order = {'type': 'milk', 'cash': 12.5, 'price': 2.0, 'ratio': 5.0}
        expected = {'milk': 6, 'violet': 0, 'espresso': 0}
        self.assertEqual(OrderProcessor.process_order(order), expected)

    def test_process_bonus(self):
        order = {'type': 'milk', 'cash': 12.5, 'price': 2.0, 'ratio': 5.0}
        expected = 1
        self.assertEqual(OrderProcessor.process_bonus(order), expected)




