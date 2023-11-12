from data import load_orders, pair_processing

def main():
    order_pairs = pair_processing(load_orders())

    reports = []
    for order, processor in order_pairs:
        reports.append(processor(order))

    for report in reports:
        string = ''
        for key, value in report.items():
            string += f'{key} {value}, '
        string = string[:-2]
        print(string)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
