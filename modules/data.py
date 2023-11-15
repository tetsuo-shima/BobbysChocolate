import copy
import csv
from resources.constants import ORDER_FILE


def _read_csv(datafile=ORDER_FILE):
    with open(datafile, 'r') as file:
        return [order for order in csv.DictReader(file)]


def _cast_integers(orders: list):
    new_orders = copy.deepcopy(orders)
    for order in new_orders:
        for key, value in order.items():
            try:
                order[key] = int(value)
            except ValueError:
                pass

    return new_orders


def load_orders(datafile=ORDER_FILE):
    orders = _read_csv(datafile)
    return _cast_integers(orders)
