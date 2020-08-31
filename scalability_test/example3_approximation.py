import threading
import time
from concurrent.futures.thread import ThreadPoolExecutor
import matplotlib.pyplot as plt


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
        with self.lock:
            value = self.value

        return value


class ApproximateCounter:

    def __init__(self, global_counter):
        self.value = 0
        self.lock = threading.Lock()
        self.global_counter = global_counter
        self.threshold = 10

    def increment(self, x):
        with self.lock:
            new_value = self.value
            time.sleep(0.001)
            self.value = new_value + x

            if self.value >= self.threshold:
                self.global_counter.increment(self.value)
                self.value = 0

    def get_value(self):
        with self.lock:
            value = self.value

        return value


def main():
    ###########################################################################
    # Previous single-lock counter

    single_counter_n_threads = []
    single_counter_times = []
    for n_workers in range(1, 11):
        single_counter_n_threads.append(n_workers)

        counter = LockedCounter()

        start = time.time()

        with ThreadPoolExecutor(max_workers=n_workers) as executor:
            executor.map(counter.increment,
                         [1 for i in range(100 * n_workers)])

        single_counter_times.append(time.time() - start)

    ###########################################################################
    # New approximate counters

    def thread_increment(counter):
        counter.increment(1)

    approx_counter_n_threads = []
    approx_counter_times = []
    for n_workers in range(1, 11):
        approx_counter_n_threads.append(n_workers)

        global_counter = LockedCounter()

        start = time.time()

        local_counters = [ApproximateCounter(global_counter)
                          for i in range(n_workers)]
        with ThreadPoolExecutor(max_workers=n_workers) as executor:
            for i in range(100):
                executor.map(thread_increment, local_counters)

        approx_counter_times.append(time.time() - start)

        print(f'Number of threads: {n_workers}')
        print(f'Final counter: {global_counter.get_value()}.')
        print('-' * 40)

    ###########################################################################
    # Plotting

    single_counter_line, = plt.plot(
        single_counter_n_threads,
        single_counter_times,
        c='blue',
        label='Single counter'
    )
    approx_counter_line, = plt.plot(
        approx_counter_n_threads,
        approx_counter_times,
        c='red',
        label='Approximate counter'
    )
    plt.legend(handles=[single_counter_line, approx_counter_line], loc=2)
    plt.xlabel('Number of threads'); plt.ylabel('Time in seconds')
    plt.show()


if __name__ == '__main__':
    main()
