import unittest
import order_processing_strategy_fn
from enum import Enum


class ChocolateType(Enum):
    milk = 1
    violet = 2
    espresso = 3
    ruby = 4


class TestOrderProcessingStrategy(unittest.TestCase):

    def test_milk_order_with_bonus(self):
        order = {'type': 'milk', 'cash': 12, 'price': 2, 'ratio': 5}
        expected = {'milk': 7, 'violet': 0, 'espresso': 0}
        self.assertEqual(order_processing_strategy_fn.
                         process_milk_order_with_bonus(order), expected)

    def test_violet_order_with_bonus(self):
        order = {'type': 'violet', 'cash': 13, 'price': 4, 'ratio': 1}
        expected = {'milk': 0, 'violet': 9, 'espresso': 0}
        self.assertEqual(order_processing_strategy_fn.
                         process_violet_order_with_bonus(order), expected)

    def test_bubkjj(self):
        order = {'type': 'espresso', 'cash': 6, 'price': 2, 'ratio': 2}
        expected = {'milk': 1, 'violet': 0, 'espresso': 4}
        self.assertEqual(order_processing_strategy_fn.
                         process_espresso_order_with_bonus(order), expected)

    def test_ruby_order_with_bonus(self):
        order = {'type': 'ruby', 'cash': 21, 'price': 2, 'ratio': 4}
        expected = {'milk': 2, 'violet': 2, 'espresso': 2, 'ruby': 12}
        self.assertEqual(order_processing_strategy_fn.
                         process_ruby_order_with_bonus(order, ChocolateType),
                         expected)
