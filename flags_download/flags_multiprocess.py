"""
Запуск загрузки флагов в потоках.

AlTheOne [https://AlTheOne.pro/]
AlTheOne.official@gmail.com
"""
__author__ = 'AlTheOne'


from concurrent import futures

from flags_download.flags import (
    save_flag, get_flag, show, main,
)


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')

    return cc


def download_many(cc_list):
    with futures.ProcessPoolExecutor() as executer:
        res = executer.map(download_one, sorted(cc_list))

    return len(list(res))


if __name__ == '__main__':
    main(download_many)
