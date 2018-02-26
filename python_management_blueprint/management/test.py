import aiohttp
import asyncio
import async_timeout


async def fetch(session, url):
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()


async def execute_request(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        print('oi')

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*[execute_request('http://python.org'),
                                       execute_request('http://python.org'),
                                       execute_request('http://python.org'),
                                       execute_request('http://python.org')]))
