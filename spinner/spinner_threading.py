import threading
import itertools
import time
import sys


class Signal:
    go = True


def spin(msg: str, signal: Signal) -> None:
    """
    Анимация спиннера.
    """
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = '{} {}'.format(char, msg)
        write(status)
        flush()
        write('\x08' * len(status))
        time.sleep(.1)

        if not signal.go:
            break

    write(' ' * len(status) + '\x08' * len(status))


def slow_func() -> int:
    """
    Для имитации ожидания завершения длителеной операции I/O.
    """
    time.sleep(3)
    return 42


def supervisor() -> int:
    """
    Менеджер операци.

    :return: Ответ думателя!
    :rtype: int
    """
    signal = Signal()
    spinner = threading.Thread(target=spin, args=('Thinking...', signal))
    print('spinner object:', spinner)

    spinner.start()
    result = slow_func()
    signal.go = False
    spinner.join()

    return result


def main():
    result = supervisor()
    print('Answer:', result)


if __name__ == '__main__':
    main()
