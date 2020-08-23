import asyncio
import time


async def count_down(name, delay, start):
    indents = (ord(name) - ord('A')) * '\t'

    n = 3
    while n:
        await asyncio.sleep(delay)

        duration = time.perf_counter() - start
        print('-' * 40)
        print('{:.4f} \t{}{} = {}'.format(duration, indents, name, n))

        n -= 1


def main():
    loop = asyncio.get_event_loop()
    start = time.perf_counter()
    tasks = [
        loop.create_task(count_down('A', 1, start)),
        loop.create_task(count_down('B', 0.8, start)),
        loop.create_task(count_down('C', 0.5, start))
    ]

    loop.run_until_complete(asyncio.wait(tasks))


if __name__ == '__main__':
    main()
