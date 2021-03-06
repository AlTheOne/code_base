import threading
import time


class MyThread(threading.Thread):

    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self) -> None:
        print('Starting thread {}'.format(self.name))
        thread_count_down(self.name, self.delay)
        print('Finished thread {}'.format(self.name))


def thread_count_down(name, delay):
    counter = 5
    while counter:
        time.sleep(delay)
        print('Thread {} counting down: {}...'.format(name, counter))
        counter -= 1


def main():
    thread1 = MyThread('AAA', 2)
    thread2 = MyThread('BBB', 1)
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('Finished.')


if __name__ == '__main__':
    main()
