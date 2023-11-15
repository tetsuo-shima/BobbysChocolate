"""
This application reads a CSV representing orders for chocolate. It displays
reports for the completed orders, which are processed based on the type of
chocolate and on sales promotion status.
"""

from modules.data import load_orders
from modules.order_processing_factory import match_processing


def main():
    """
    Output reports of processes orders
    :return: None
    """
    orders = match_processing(load_orders())

    reports = [order.process(order.data) for order in orders]

    for report in reports:
        results = [f'{key} {value}, ' for key, value in report.items()]
        print(''.join(results)[:-2])


if __name__ == '__main__':
    main()
