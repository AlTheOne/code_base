import queue
import threading
import time


class MyThread(threading.Thread):
    """
    Пользовательский поток.
    """

    def __init__(self, name: str, q: queue.Queue):
        """
        Принимает имя для потока и очередь из
        которой будем брать данные для запуска задач.

        :param name: Имя потока.
        :type name: str
        :param q: Объект очереди.
        :type q: queue.Queue
        """
        super().__init__()
        self.name = name
        self.q = q

    def run(self) -> None:
        print('Starting thread {}'.format(self.name))
        process_queue(self.name, self.q)
        print('Finished thread {}'.format(self.name))


def process_queue(thread_name: str, my_queue: queue.Queue) -> None:
    """
    Извлечение данных из очереди.

    :param thread_name: Имя потока, который запрашивает данные.
    :type thread_name: str
    :param my_queue: Объект очереди.
    :type my_queue: queue.Queue
    """
    while True:
        try:
            x = my_queue.get(block=False)
        except queue.Empty:
            return
        else:
            print_factors(thread_name, x)

        time.sleep(1)


def print_factors(thread_name: str, x: int) -> None:
    """
    Нахождение множителей значения x.

    :param thread_name: Имя потока, который запрашивает данные.
    :type thread_name: str
    :param x: Значение.
    :type x: int
    """
    results_str = ['{}: Positive factors of {} are:'.format(thread_name, x)]
    for i in range(1, x+1):
        if x % i == 0:
            results_str.append(str(i))

    results_str.append('\n')
    results_str.append('_' * 20)

    print(' '.join(results_str))


def main():
    data = [1, 10, 4, 3, 21, 22, 24]

    my_queue = queue.Queue()
    for x in data:
        my_queue.put(x)

    thread1 = MyThread('AAA', my_queue)
    thread2 = MyThread('BBB', my_queue)
    thread3 = MyThread('CCC', my_queue)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    print('Done.')


if __name__ == '__main__':
    main()
