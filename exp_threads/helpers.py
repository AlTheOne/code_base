from math import sqrt


def is_prime(x: int) -> None:
    """
    Проверки является ли неотрицательное число простым.

    :param x: Проверяемое значение.
    :type x: int
    """
    if x < 2:
        print('{} is not a prime number.'.format(x))

    elif x == 2:
        print('{} is a prime number.'.format(x))

    elif x % 2 == 0:
        print('{} is not a prime number.'.format(x))

    else:
        limit = int(sqrt(x)) + 1
        for i in range(3, limit, 2):
            if x % i == 0:
                print('{} is not a prime number.'.format(x))
                return

        print('{} is a prime number.'.format(x))
