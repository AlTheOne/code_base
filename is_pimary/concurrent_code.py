from concurrent import futures
from timeit import default_timer as timer

from is_pimary.helpers import is_prime


def main():
    input_seq = [i for i in range(10 ** 13, 10 ** 13 + 500)]

    start = timer()
    result = []

    with futures.ProcessPoolExecutor() as executor:
        future_list = [executor.submit(is_prime, i)
                       for i in input_seq]

        for i, future in enumerate(futures.as_completed(future_list)):
            if future.result():
                result.append(input_seq[i])

    print('Result 2:', result)
    print('Took: %.2f seconds.' % (timer() - start))


if __name__ == '__main__':
    main()
