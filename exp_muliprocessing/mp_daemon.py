import time
from multiprocessing import Process

from exp_muliprocessing.mp_current_process import f1, f2


def main():
    p1 = Process(name='Worker 1', target=f1)
    p1.daemon = True
    p2 = Process(name='Worker 2', target=f2)

    p1.start()
    time.sleep(1)
    p2.start()

    p1.join(1)
    print('Whether Worker 1 is still alive:', p1.is_alive())
    p2.join()


if __name__ == '__main__':
    main()
