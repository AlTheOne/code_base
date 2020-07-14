import os
from concurrent import futures
from timeit import default_timer as timer

from is_pimary.helpers import is_prime


def concurrent_solve(n_workers, data):
    print('Number of workers: {}'.format(n_workers))

    start = timer()
    result = []
    with futures.ProcessPoolExecutor(max_workers=n_workers) as executor:
        future_list = [executor.submit(is_prime, i) for i in data]
        completed_futures = futures.as_completed(future_list)

        sub_start = timer()

        for i, future in enumerate(completed_futures):
            if future.result():
                result.append(future.result())

        sub_duration = timer() - sub_start
        print('Sub took: {:.5f} seconds'.format(sub_duration))
        print('Took: {:.5f} seconds'.format(timer() - start))


def main():
    data = range(10 ** 13, 10 ** 13 + 1000)
    for n_worker in range(1, os.cpu_count()+1):
        concurrent_solve(n_worker, data)
        print('_' * 30)


if __name__ == '__main__':
    main()
