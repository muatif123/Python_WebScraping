import aiohttp
import async_timeout
import asyncio
import time


async def fetch_page(session, url):
    page_start = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            print(f'Page took {time.time() - page_start}')
            return response.status


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks

loop = asyncio.get_event_loop()

tasks = [fetch_page('http://google.com') for i in range(50)]
start = time.time()
loop.run_until_complete(asyncio.gather(*tasks))
print(f'All took {time.time() - start}')