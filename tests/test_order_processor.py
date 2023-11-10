import unittest
from collections import OrderedDict

from order_processor import ChocolateType, OrderProcessor


class TestOrderProcessor(unittest.TestCase):
    def test_process_order(self):
        order = {'type': 'milk', 'cash': 12, 'price': 2, 'ratio': 5}
        expected = {'milk': 6, 'violet': 0, 'espresso': 0}
        self.assertEqual(OrderProcessor.process_order(order), expected)
