import threading
import time

from is_pimary.helpers import is_prime


class MyThread(threading.Thread):

    def __init__(self, value):
        super().__init__()
        self.value = value

    def run(self) -> None:
        print('Starting process with value {}'.format(self.value))
        is_prime(self.value)
        print('Finished process with value {}'.format(self.value))


def main():
    data_list = [2, 193, 323, 1327, 433785907]
    for data in data_list:
        thread = MyThread(data)
        thread.start()
        thread.join()

    print('Finished.')


if __name__ == '__main__':
    main()
