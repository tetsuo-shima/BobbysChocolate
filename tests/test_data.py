import unittest
from data import Data

filename = 'test_resources/test_orders.csv'


class TestData(unittest.TestCase):
    def test_read_file(self):
        orders = Data.load_orders(filename)
        first = {'type': 'milk', 'cash': 12.1, 'price': 2, 'ratio': 5}
        second = {'type': 'violet', 'cash': 13, 'price': 4, 'ratio': 1}
        third = {'type': 'espresso', 'cash': 6, 'price': 2, 'ratio': 2}
        self.assertEqual(orders, [first, second, third])
