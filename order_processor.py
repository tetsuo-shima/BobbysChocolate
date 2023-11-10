from enum import Enum


class ChocolateType(Enum):
    milk = 1
    violet = 2
    espresso = 3


class OrderProcessor:
    @staticmethod
    def process_order(order: dict) -> dict:
        order_sheet = {chocolate_type.name: 0 for chocolate_type in
                       ChocolateType}

        for key in order_sheet.keys():
            if key == order['type']:
                order_sheet[key] = order['cash'] // order['price']

        return order_sheet

