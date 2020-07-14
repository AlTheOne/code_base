from timeit import default_timer as timer

from is_pimary.helpers import is_prime


def main():
    input_seq = [i for i in range(10 ** 13, 10 ** 13 + 500)]

    start = timer()
    result = []
    for i in input_seq:
        if is_prime(i):
            result.append(i)
    print('Result 1:', result)
    print('Took: %.2f seconds.' % (timer() - start))


if __name__ == '__main__':
    main()
