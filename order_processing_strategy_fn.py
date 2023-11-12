from chocolate_type import ChocolateType
from abc import ABC, abstractmethod


def _create_blank_report(flavors: ChocolateType) -> dict:
    return {flavor.name: 0 for flavor in flavors}


def _calculate_quantity(order) -> int:
    return order['cash'] // order['price']


def _process_bonus(order) -> int:
    return _calculate_quantity(order) // order['ratio']


def process_regular_order(order, flavor=ChocolateType):
    report = _create_blank_report(flavor)

    for key in report.keys():
        if key == order['type']:
            report[key] = _calculate_quantity(order)

    return report


def process_milk_order_with_bonus(order, flavor=ChocolateType):
    report = _create_blank_report(flavor)

    for key in report.keys():
        if key == order['type']:
            report[key] = (_calculate_quantity(order) +
                           _process_bonus(order))

    return report


def process_violet_order_with_bonus(order, flavor=ChocolateType):
    report = _create_blank_report(flavor)

    for key in report.keys():
        if key == order['type']:
            report[key] = (_calculate_quantity(order) +
                           (2 * _process_bonus(order)))

    return report


def process_espresso_order_with_bonus(order, flavor=ChocolateType):
    report = _create_blank_report(flavor)
    bonus = _process_bonus(order)

    for key in report.keys():
        if key == order['type']:
            report[key] = _calculate_quantity(order) + bonus
    report['milk'] = bonus

    return report


def process_ruby_order_with_bonus(order, flavor=ChocolateType):
    report = _create_blank_report(flavor)
    bonus = _process_bonus(order)

    for key in report.keys():
        report[key] = bonus
        if key == order['type']:
            report[key] += _calculate_quantity(order)

    return report
