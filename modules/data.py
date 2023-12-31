""" functions to read in dictionaries from CSV"""
from typing import List, Dict
from csv import DictReader
from resources.constants import ORDER_FILE


def _read_csv(datafile: str = ORDER_FILE) -> List[dict]:
    """
    :param datafile: :param datafile: path to file to be read
    :return: list of dictionaries representing lines in file; value in
    key:value is a string
    """
    with open(datafile, 'r') as file:
        return list(DictReader(file))


def _cast_integers(orders: List[dict]) -> List[Dict]:
    """
    :param orders: list of dictionaries read from CSV. Given 'key: value',
    all values read by DictReader as strings e.g. '1'
    :return: list of dictionaries in which values are cast integers when
    appropriate
    """
    for order in orders:
        for key, value in order.items():
            try:
                order[key] = int(value)
            except ValueError:
                pass

    return orders


def load_orders(datafile: str = ORDER_FILE) -> List[dict]:
    """
    :param datafile: path to file to be read
    :return: list of dictionaries representing lines in file
    """
    orders = _read_csv(datafile)
    return _cast_integers(orders)
