"""
Множественная отправка HTTP GET запросов
с использованием потоков.

AlTheOne [https://AlTheOne.pro/]
AlTheOne.official@gmail.com
"""
__author__ = 'AlTheOne'

from concurrent import futures

import argparse
import sys
import requests


version = '0.0.1'


def create_parser():
    """
    Создание парсера для аргументов командной строки.

    :return: Парсер.
    :rtype: argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser(
        description='Программа для отправки HTTP запросов с помощью потоков.',
    )
    parser.add_argument('-u', '--url', required=True, type=str)
    parser.add_argument('-w', '--workers', default=100, type=int)
    parser.add_argument('-r', '--requests', default=100, type=int)

    return parser


def func_request(url: str, num: int) -> tuple:
    """
    Выполнение запросов.

    :param url: Целевая ссылка.
    :type url: str
    :param num: Порядковый номер запроса.
    :type num: int

    :return: номер запроса и HTTP ответ.
    :rtype: tuple
    """
    response = requests.get(url)
    return num, response


def signal(future: futures._base.Future) -> None:
    """
    Оповещение о завершении работы потока.

    :param future: Объект с результатами.
    :type future: concurrent.futures._base.Future
    """
    num, response = future.result()
    print('Запрос #{} - <ID: {}> - {!r}'.format(num, id(future), response))


def main(url: str, max_workers: int = 100, req_counter: int = 100) -> None:
    """
    Запуск задач.

    :param url: Целевая ссылка.
    :type url: str
    :param max_workers: Количество воркеров в пуле потоков.
    :type max_workers: int
    :param req_counter: Количество запросов.
    :type req_counter: int
    """
    print('Начало работы...')

    with futures.ThreadPoolExecutor(max_workers=max_workers) as executer:
        for i in range(req_counter):
            future = executer.submit(func_request, url, i)
            future.add_done_callback(signal)

    print('Работа окончена:\n URL: {}\n Запросов: {}\n Потоков: {}'.format(
        url, max_workers, req_counter,
    ))


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])

    main(
        url=namespace.url,
        max_workers=namespace.workers,
        req_counter=namespace.requests,
    )
