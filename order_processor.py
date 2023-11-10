from enum import Enum


class ChocolateType(Enum):
    milk = 1
    violet = 2
    espresso = 3


class OrderProcessor:
    @staticmethod
    def create_order_sheet(flavors=ChocolateType) -> dict:
        return {flavor.name: 0 for flavor in flavors}

    @staticmethod
    def process_order(order: dict, bonus: bool = False) -> dict:
        order_sheet = OrderProcessor.create_order_sheet()

        for key in order_sheet.keys():
            if key == order['type']:
                order_sheet[key] = OrderProcessor._calculate_quantity(order)
                if bonus:
                    order_sheet[key] += OrderProcessor.process_bonus(order)

        return order_sheet

    @staticmethod
    def _calculate_quantity(order) -> int:
        return order['cash'] // order['price']

    @staticmethod
    def process_bonus(order) -> int:
        return OrderProcessor._calculate_quantity(order) // order['ratio']
