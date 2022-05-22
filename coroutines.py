import asyncio
import time
import unittest
import random


class CoroutinesTest(unittest.TestCase):
    """ python的协程 """

    async def crawl_page(self, url):
        print('crawling {}'.format(url))
        sleep_time = int(url.split('_')[-1])
        await asyncio.sleep(sleep_time)
        print('OK {}'.format(url))

    async def call_crawl_page(self):
        urls = ['url_1', 'url_2', 'url_3', 'url_4']
        # for url in urls:
        #     await self.crawl_page(url)
        tasks = [asyncio.create_task(self.crawl_page(url)) for url in urls]
        await asyncio.gather(*tasks)

    def test_crawl_page(self):
        t1 = time.perf_counter()
        asyncio.run(self.call_crawl_page())
        t2 = time.perf_counter()
        print(f'cost time: {t2-t1}')

    async def worker_1(self):
        await asyncio.sleep(1)
        return 1

    async def worker_2(self):
        await asyncio.sleep(2)
        return 2 / 0

    async def worker_3(self):
        await asyncio.sleep(3)
        return 3

    async def call_workers(self):
        task_1 = asyncio.create_task(self.worker_1())
        task_2 = asyncio.create_task(self.worker_2())
        task_3 = asyncio.create_task(self.worker_3())

        await asyncio.sleep(2)
        task_3.cancel()

        res = await asyncio.gather(task_1, task_2, task_3, return_exceptions=True)
        print(res)

    def test_workers(self):
        t1 = time.perf_counter()
        asyncio.run(self.call_workers())
        t2 = time.perf_counter()
        print(f'cost time: {t2-t1}')

    async def consumer(self, queue, id):
        while True:
            val = await queue.get()
            print(f'{id} get a val: {val}')
            await asyncio.sleep(1)

    async def producer(self, queue, id):
        for i in range(5):
            val = random.randint(1, 10)
            await queue.put(val)
            print(f'{id} put a val: {val}')
            await asyncio.sleep(1)

    async def call_producer_consumer(self):
        queue = asyncio.Queue()
        consumer_1 = asyncio.create_task(self.consumer(queue, 'consumer_1'))
        consumer_2 = asyncio.create_task(self.consumer(queue, 'consumer_2'))
        producer_2 = asyncio.create_task(self.producer(queue, 'producer_2'))
        producer_1 = asyncio.create_task(self.producer(queue, 'producer_1'))
        await asyncio.sleep(10)
        consumer_1.cancel()
        consumer_2.cancel()
        await asyncio.gather(consumer_1, consumer_2, producer_1, producer_2, return_exceptions=True)

    def test_producer_consumer(self):
        asyncio.run(self.call_producer_consumer())


if __name__ == '__main__':
    unittest.main()
