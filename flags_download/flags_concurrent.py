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

MAX_WORKERS = 20


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def concurrent_complited(future):
    print('{}: ОНА ВЫПОЛНИЛАСЬ!!!!!!!!'.format(future))


# # Альтернатива на .map
# def download_many(cc_list):
#     workers = min(MAX_WORKERS, len(cc_list))
#     with futures.ThreadPoolExecutor(workers) as executer:
#         res = executer.map(download_one, sorted(cc_list))
#
#     return len(list(res))


def download_many(cc_list):
    with futures.ThreadPoolExecutor(max_workers=3) as executer:
        to_do = []
        for cc in sorted(cc_list):
            future = executer.submit(download_one, cc)
            future.add_done_callback(concurrent_complited)
            to_do.append(future)
            msg = 'Sheduled for {}: {}'
            print(msg.format(cc, future))

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)

    return len(results)


if __name__ == '__main__':
    main(download_many)
