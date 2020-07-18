from multiprocessing import Process, current_process
import time
import os


def print_info(title):
    print(title)

    if hasattr(os, 'getppid'):
        print('Parent process ID: {}.'.format(os.getppid()))

    print('Current Process ID: {}.\n'.format(os.getpid()))


def f():
    print_info('Function f')

    pname = current_process().name
    print('Starting process %s...' % pname)
    time.sleep(2)
    print('Exiting process %s...' % pname)


def main():
    print_info('Main program')

    p1 = Process(target=f)
    p1.start()
    p1.join()


if __name__ == '__main__':
    main()
