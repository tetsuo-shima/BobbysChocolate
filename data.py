import csv
from order_processing_strategy_fn import (process_regular_order,
                                          process_milk_order_with_bonus as
                                          milk_bonus,
                                          process_violet_order_with_bonus as
                                          violet_bonus,
                                          process_espresso_order_with_bonus as
                                          espresso_bonus,
                                          process_ruby_order_with_bonus as
                                          ruby_bonus)
from constants import ORDER_FILE, BONUS_PROMOTION_ACTIVATED


def load_orders(datafile=ORDER_FILE):
    with open(datafile, 'r') as file:
        csv_reader = csv.DictReader(file)
        orders = [order for order in csv_reader]
    for order in orders:
        for key, value in order.items():
            try:
                order[key] = int(value)
            except ValueError:
                pass

    return orders

# TODO: add test for this
def pair_processing(orders: list) -> list:
    processing_pairs = []
    for order in orders:
        if BONUS_PROMOTION_ACTIVATED:
            if order['type'] == 'ruby':
                pair = (order, ruby_bonus)
            elif order['type'] == 'milk':
                pair = (order, milk_bonus)
            elif order['type'] == 'violet':
                pair = (order, violet_bonus)
            elif order['type'] == 'espresso':
                pair = (order, espresso_bonus)
        else:
            pair = (order, process_regular_order)

        processing_pairs.append(pair)

    return processing_pairs
