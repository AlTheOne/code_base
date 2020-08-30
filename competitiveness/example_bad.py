import random
import threading
import time

counter = 0


def update():
    global counter

    current_counter = counter
    time.sleep(random.randint(0, 1))
    counter = current_counter + 1


def main():
    threads = [threading.Thread(target=update) for i in range(20)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Final counter: {counter}.')
    print('Finished.')


if __name__ == '__main__':
    main()
