import _thread as thread

from exp_threads.helpers import is_prime


def main() -> None:
    my_input = [2, 193, 323, 1327, 433785907]
    for i in my_input:
        thread.start_new_thread(is_prime, (i,))

    # Disadvantage: input() need for waiting result of threads
    input('Type something to quit: \n')
    print('Finished.')


if __name__ == '__main__':
    main()
