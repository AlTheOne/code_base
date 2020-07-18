from math import sqrt
import multiprocessing


class Consumer(multiprocessing.Process):

    def __init__(self, task_queue, result_queue):
        super().__init__()
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        pname = self.name

        while not self.task_queue.empty():
            current_task = self.task_queue.get()

            if current_task is None:
                print('Exiting {}...'.format(pname))
                self.task_queue.task_done()
                break

            print('{} prcessing task: {}'.format(pname, current_task))

            answer = current_task.process()
            self.task_queue.task_done()
            self.result_queue.put(answer)


class Task:
    def __init__(self, x):
        self.x = x

    def process(self):
        msg_is_prime = '{} is a prime number'
        msg_is_not_prime = '{} is not a prime number'
        if self.x < 2:
            return msg_is_not_prime.format(self.x)

        if self.x == 2:
            return msg_is_prime.format(self.x)

        if self.x % 2 == 0:
            return msg_is_not_prime.format(self.x)

        limit = int(sqrt(self.x)) + 1
        for i in range(3, limit, 2):
            if self.x % i == 0:
                return msg_is_not_prime.format(self.x)

        return msg_is_prime.format(self.x)

    def __str__(self):
        return 'Checking if {} is a prime or not'.format(self.x)


def main():
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    n_consumers = multiprocessing.cpu_count()
    print('Spawning {} consumers...'.format(n_consumers))
    consumers = [Consumer(tasks, results) for i in range(n_consumers)]
    for consumer in consumers:
        consumer.start()

    my_input = [2, 36, 101, 193, 323, 513, 1327, 100000, 9999999, 433785907]
    for item in my_input:
        tasks.put(Task(item))

    # poison pill
    for i in range(n_consumers):
        tasks.put(None)

    tasks.join()

    for i in range(len(my_input)):
        temp_result = results.get()
        print('Result:', temp_result)

    print('Done.')


if __name__ == '__main__':
    main()
