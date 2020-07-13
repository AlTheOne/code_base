"""
Запуск спящей функции и спиннера загрузки
на основе asyncio.

AlTheOne [https://AlTheOne.pro/]
AlTheOne.official@gmail.com
"""
__author__ = 'AlTheOne'

import asyncio
import itertools


async def spin(msg: str) -> None:
    """
    Анимация спиннера.
    """
    for char in itertools.cycle('|/-\\'):
        status = '{} {}'.format(char, msg)
        print(status, flush=True, end='\r')

        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break

    print(' ' * len(status), end='\r')


async def slow_func() -> int:
    """
    Для имитации ожидания завершения длителеной операции I/O.
    """
    await asyncio.sleep(3)
    return 42


async def supervisor() -> int:
    """
    Менеджер операци.

    :return: Ответ думателя!
    :rtype: int
    """
    spinner = asyncio.create_task(spin('thinking...'))
    print('Spinner object:', spinner)
    result = await slow_func()
    spinner.cancel()

    return result


def main():
    result = asyncio.run(supervisor())
    print('Answer:', result)


if __name__ == '__main__':
    main()
