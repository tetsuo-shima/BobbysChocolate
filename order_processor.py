from chocolate_type import ChocolateType

#TODO: Delete this file after checking dependencies
def create_order_sheet(flavors=ChocolateType) -> dict:
    return {flavor.name: 0 for flavor in flavors}


def process_order(order: dict, bonus: bool = False) -> dict:
    order_sheet = create_order_sheet()

    for key in order_sheet.keys():
        if key == order['type']:
            order_sheet[key] = _calculate_quantity(order)
            if bonus:
                order_sheet[key] += process_bonus(order)

    return order_sheet


def _calculate_quantity(order) -> int:
    return order['cash'] // order['price']


def process_bonus(order) -> int:
    return _calculate_quantity(order) // order['ratio']
