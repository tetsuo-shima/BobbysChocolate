import unittest
import modules.data

filename = 'test_resources/test_orders.csv'


class TestData(unittest.TestCase):

    def test_read_csv(self):
        actual = modules.data._read_csv(filename)
        expected = [
            {'type': 'milk', 'cash': '12.1', 'price': '2', 'ratio': '5'},
            {'type': 'violet', 'cash': '13', 'price': '4', 'ratio': '1'},
            {'type': 'espresso', 'cash': '6', 'price': '2', 'ratio': '2'}
        ]
        self.assertEqual(actual, expected)

    def test_cast_integers(self):
        order_list = [
            {'type': 'milk', 'cash': '12.1', 'price': '2', 'ratio': '5'},
            {'type': 'violet', 'cash': '13', 'price': '4', 'ratio': '1'},
            {'type': 'espresso', 'cash': '6', 'price': '2', 'ratio': '2'}
        ]
        actual = modules.data._cast_integers(order_list)
        expected = [
            {'type': 'milk', 'cash': 12.1, 'price': 2, 'ratio': 5},
            {'type': 'violet', 'cash': 13, 'price': 4, 'ratio': 1},
            {'type': 'espresso', 'cash': 6, 'price': 2, 'ratio': 2}
        ]
        self.assertEqual(actual, expected)

    def test_read_file(self):
        orders = modules.data.load_orders(filename)
        first = {'type': 'milk', 'cash': 12.1, 'price': 2, 'ratio': 5}
        second = {'type': 'violet', 'cash': 13, 'price': 4, 'ratio': 1}
        third = {'type': 'espresso', 'cash': 6, 'price': 2, 'ratio': 2}
        self.assertEqual(orders, [first, second, third])
