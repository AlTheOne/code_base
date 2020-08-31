import time
from concurrent.futures.thread import ThreadPoolExecutor
import matplotlib.pyplot as plt

from scalability_test.example1_counter import LockedCounter


def main():

    n_threads = []
    times = []
    for n_workers in range(1, 11):
        n_threads.append(n_workers)

        counter = LockedCounter()

        start = time.time()

        with ThreadPoolExecutor(max_workers=n_workers) as executor:
            executor.map(counter.increment,
                         [1 for i in range(100 * n_workers)])

        times.append(time.time() - start)

        print(f'Number of threads: {n_workers}')
        print(f'Final counter: {counter.get_value()}.')
        print(f'Time taken: {times[-1] : .2f} seconds.')
        print('-' * 40)

    plt.plot(n_threads, times)
    plt.xlabel('Number of threads'); plt.ylabel('Time in seconds')
    plt.show()


if __name__ == '__main__':
    main()
