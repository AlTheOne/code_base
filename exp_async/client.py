import aiohttp
import asyncio


async def get_html(session, url):
    async with session.get(url, ssl=False) as res:
        return await res.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await get_html(session, 'http://altheone.pro')
        print(html)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
