import asyncio
import json
import os
import random
import string
import time

import aiohttp


async def main(fut):
    print(f'{time.ctime()} main says: Hello! I have future!')
    print(f"Future done? -->", fut.done())
    await asyncio.sleep(1.0)
    fut.set_result("Future AHEAD!")
    print(f"Future done? -->", fut.done())
    print(f'{time.ctime()} Future AHEAD!')
    print(f'{time.ctime()} main says:  Goodbye!')


async def second_action():
    print(f'{time.ctime()} Second action starts!')
    print(f'{time.ctime()} GOOD NEWS! This action also has future ')
    await asyncio.sleep(1.5)
    print(f'{time.ctime()} Second action stopped')


async def get_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            assert res.status == 200
            return await res.read()


async def get_reddit_top(subreddit):
    data1 = await get_json(url='https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5')

    j = json.loads(data1.decode('utf-8'))
    for i in j['data']['children']:
        title = i['data']['title']
        link = i['data']['url']
        print(f"{time.ctime()} Be serious! Few words about {subreddit}!")
        print(f"{title}  {link}")


async def fetch_pic():
    url = 'https://picsum.photos/400/600'
    path = os.path.join(os.getcwd(), 'img')
    random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            if res.status == 200:
                print(f'{time.ctime()} PICTURE? Yeah, start download {random_name}.jpg')
                test = await res.read()
                with open(f'{path}/{random_name}.jpg', mode='wb') as f:
                    f.write(test)
            else:
                print("Data fetch failed")
                print("Status", res.status)


async def future_actions(count):
    for i in range(count):
        print(f"{time.ctime()} Future tasks? It's spinning my head..." )
        asyncio.ensure_future(fetch_pic())


async def add_joke(url, headers):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                result = await response.json()
                print(f'{time.ctime()} Time for joking: {result["joke"]}')
            else:
                print("Data fetch failed")
                print("Status", response.status)


async def something_that_stop(loop, seconds, future):
    print(f'{time.ctime()} Stopper: I like to stop this in {seconds} sec')
    await asyncio.sleep(seconds)
    print(f'{time.ctime()} Stopper: All stops now!')
    future.set_result("Hoorah")
    print(f'{time.ctime()} finish...{future} {future.done()}')
    loop.stop()


def some_blocking_func():
    """I can't block too long, they should wait while I'll finish"""
    time.sleep(5)
    print(f"{time.ctime()} A have started blocking NOW!!!")


url = "https://icanhazdadjoke.com/"
headers = {"accept": "application/json"}


print(f"{time.ctime()} Lets start the journey in AsyncIO")
fut = asyncio.Future()
future = asyncio.Future()
loop = asyncio.get_event_loop()
loop.create_task(something_that_stop(loop, 6, future))
loop.create_task(main(fut))
loop.create_task(second_action())
loop.create_task(get_reddit_top("python"))
loop.create_task(add_joke(url, headers=headers))
loop.create_task(future_actions(3))
loop.run_in_executor(None, some_blocking_func)
loop.run_forever()
loop.close()

# async def async_worker(seconds):
#     print('Sleep using {}'.format(seconds))
#     await asyncio.sleep(seconds)
#     print('Done sleep: {}'.format(seconds))
#
#
# async def stop_event_loop(loop, seconds):
#     print('Stop in {}s'.format(seconds))
#     await asyncio.sleep(seconds)
#     loop.stop()
#     print('Stopped')
#
#
# async def resolve_future(future):
#     await asyncio.sleep(5)
#     print('Future set_result')
#     future.set_result(10)
#
#
# async def wait_for_future(future):
#     result = await future
#     print('Future result: {}'.format(result))
#
#
# event_loop = asyncio.get_event_loop()
#
#
# fut = asyncio.Future()
#
# event_loop.create_task(async_worker(3))
# event_loop.create_task(async_worker(4))
#
# event_loop.create_task(stop_event_loop(event_loop, 13))
#
# event_loop.create_task(resolve_future(fut))
#
# event_loop.create_task(wait_for_future(fut))
#
# event_loop.run_forever()
# event_loop.close()