import threading
import time
from copy import deepcopy
from pprint import pprint
from random import choice


class Network:

    def __init__(self, primary_key, primary_value):
        self.primary_key = primary_key
        self.data = {primary_key: primary_value}

    def __str__(self):
        data_list = ['{\n']
        data_list.extend([f'\t{key}: {self.data[key]};\n'
                          for key in self.data])
        data_list.append('}')

        return ''.join(data_list)

    def add_node(self, key, value):
        if key not in self.data:
            self.data[key] = value
            return True

        return False

    def refresh_primary(self):
        del self.data[self.primary_key]
        self.primary_key = choice(list(self.data))

    def get_primary_value(self):
        copy_network = deepcopy(self)

        primary_key = copy_network.primary_key
        time.sleep(1)
        return copy_network.data[primary_key]

        # # Without RCU...
        # primary_key = self.primary_key
        # time.sleep(1)
        # return self.data[primary_key]


def main():
    my_network = Network('A', 1)
    for idx, i in enumerate('BCD', 2):
        my_network.add_node(i, idx)

    print(my_network)

    def print_network_primary_value():
        nonlocal my_network

        print(f'Current primary value: {my_network.get_primary_value()}.')

    thread1 = threading.Thread(target=print_network_primary_value)
    thread2 = threading.Thread(target=my_network.refresh_primary)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f'Final network: {my_network}')


if __name__ == '__main__':
    main()
