import aiohttp
import json
from .errors import *

import os
from datetime import datetime, timedelta

from .apiresponse import APIResponse


class RequestManager:
    def __init__(self, client):
        self.client = client

    async def request(self, method, url):
        await self.client.save_cache()
        running = os.getcwd()
        cache = json.load(open(running + '/.demojicache/cache.json', 'r'))
        met = cache.get(method)
        if met:
            if method in ('all', 'stats'):
                if datetime.utcnow() <= datetime.strptime(cache[method]['request_after'], "%Y-%m-%d %H:%M:%S.%f"):
                    return cache[method]['info']
                else:
                    pass
            else:
                return cache[method]['info']

        async with aiohttp.ClientSession() as session:
            async with session.request(method, url) as response:
                if response.status == 200:
                    try:
                        res = await response.json()
                        cache[method] = {}
                        cache[method]['info'] = res
                        if method in ('all', 'stats'):
                            cache[method]['request_after'] = f'{datetime.utcnow() + timedelta(minutes=30)}'
                        with open(running + '/.demojicache/cache.json', 'w') as fp:
                            json.dump(cache, fp, indent=4)
                        return res
                    except json.JSONDecodeError:
                        raise RequestFailed("Can't make request. Try again later.")
                elif response.status == 429:
                    raise RequestFailed("Can't make request. Try again later.")
