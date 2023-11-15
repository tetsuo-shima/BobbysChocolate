from collections import namedtuple

from classes.name_not_found_exception import NameNotFoundException
from modules.chocolate_type import ChocolateType as Ct
from resources.constants import BONUS_PROMOTION_ACTIVATED
from modules.order_processors import (
    process_regular_order as regular,
    process_milk_order_with_bonus as milk_bonus,
    process_violet_order_with_bonus as violet_bonus,
    process_espresso_order_with_bonus as espresso_bonus,
    process_ruby_order_with_bonus as ruby_bonus
)

processors = {
    Ct.milk.name: milk_bonus,
    Ct.violet.name: violet_bonus,
    Ct.espresso.name: espresso_bonus,
    Ct.ruby.name: ruby_bonus
}
OrderProcess = namedtuple('OrderProcess', 'data process')


def match_processing(orders: list, flavors=Ct) -> list:
    order_process_list = []
    flavor_list = [flavor.name for flavor in flavors]

    for order in orders:
        order_flavor = order['type']
        if (BONUS_PROMOTION_ACTIVATED and
                order_flavor in flavor_list):
            processor = processors[order_flavor]
        elif order_flavor in flavor_list:
            processor = regular
        else:
            raise NameNotFoundException(order.type)

        order_process_list.append(OrderProcess(data=order, process=processor))

    return order_process_list
