import csv

class Data:
    @staticmethod
    def read_file(datafile):
        with open(datafile, 'r') as file:
            csv_reader = csv.DictReader(file)
            orders = [order for order in csv_reader]
            for order in orders:
                for key, value in order.items():
                    try:
                        order[key] = float(value)
                    except ValueError:
                        pass

        return orders
