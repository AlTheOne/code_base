from multiprocessing import Process
import time


def count_down(name: str, delay: float) -> None:
    """
    Обратный отсчёт.

    :param name: Название процесса.
    :type name: str
    :param delay: Задержка.
    :type delay: float
    """

    print('Process {} starting...'.format(name))

    counter = 5
    while counter:
        time.sleep(delay)
        print('Process {} counting down: {}...'.format(name, counter))
        counter -= 1

    print('Process {} exiting...'.format(name))


def main():
    process1 = Process(target=count_down, args=('AAA', 0.5))
    process2 = Process(target=count_down, args=('BBB', 0.5))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print('Done.')


if __name__ == '__main__':
    main()
