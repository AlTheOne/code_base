import threading
import time
from concurrent.futures.thread import ThreadPoolExecutor


class LocklessCounter:

    def __init__(self):
        self.value = 0

    def increment(self, x):
        new_value = self.value
        time.sleep(0.001)
        self.value = new_value + x

    def get_value(self):
        return self.value


class LockedCounter:

    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self, x):
        with self.lock:
            new_value = self.value
            time.sleep(0.001)
            self.value = new_value + x

    def get_value(self):
        return self.value


def main():

    lockless_counter = LocklessCounter()
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(lockless_counter.increment, [1 for i in range(300)])

    locked_counter = LockedCounter()
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(locked_counter.increment, [1 for i in range(300)])

    print(f'LocklessCounter result: {lockless_counter.get_value()}')
    print(f'LockedCounter result: {locked_counter.get_value()}')


if __name__ == '__main__':
    main()
