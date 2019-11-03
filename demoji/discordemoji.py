from .errors import *
from .requestmanager import RequestManager
from .apiresponse import APIResponse

import os
import json


class Client:
    def __init__(self, use_cache=False):
        self.__using_cache = use_cache
        self.__urls = {
            "all": "https://discordemoji.com/api",
            "packs": "https://discordemoji.com/api/packs",
            "categories": "https://discordemoji.com/api?request=categories",
            "stats": "https://discordemoji.com/api?request=stats"
        }
        self.__manager = RequestManager(self)

    async def save_cache(self):
        if self.__using_cache:
            running = os.getcwd()
            if not os.path.exists(running+'/.demojicache'):
                os.mkdir(running+'/.demojicache')
            if not os.path.exists(running+'/.demojicache/cache.json'):
                open(running+'/.demojicache/cache.json', 'w')
                with open(running + '/.demojicache/cache.json', 'w') as fp:
                    obj = {}
                    json.dump(obj=obj, fp=fp, indent=4)

    async def get_all(self):
        request = await self.__manager.request('get', self.__urls.get('all'))
        response = APIResponse(request, 'search')
        return response

    async def search_by_author(self, name: str=None):
        if name is None:
            raise MissingParameter('Missing parameter "name".')
        if not isinstance(name, str):
            raise TypeError('The parameter "name" must be a string.')
        request = self.__manager.request('get', self.__urls.get('all'))
        response = await request
        results = []
        for element in response:
            if element['submitted_by'] == name:
                element['site_url'] = f"https://discordemoji.com/emoji/{element['slug']}"
                results.append(element)
        if len(results) > 0:
            return results
        elif len(results) <= 0:
            return None

    async def get_by_name(self, name: str=None):
        """
        Fetch DE Emoji by name

        Parameters
        -------
        name: str, the emoji name
            name must be case-sensitive

        Returns
        -------
        demoji.apiresponse.APIResponse
            response object with emoji information
        """
        if name is None:
            raise MissingParameter('Missing parameter "name".')
        if not isinstance(name, str):
            raise TypeError('The parameter "name" must be a string.')

        request = self.__manager.request('get', self.__urls.get('all'))
        response = await request
        for element in response:
            if element['title'] == name:
                element['site_url'] = f"https://discordemoji.com/emoji/{element['slug']}"
                return APIResponse(element, 'get')
        return None

    async def get_by_id(self, id: int=None):
        """
        Fetch DE Emoji by id

        Parameters
        -------
        id: int, the emoji id in discordemoji

        Returns
        -------
        demoji.apiresponse.APIResponse
            response object with emoji information
        """
        if id is None:
            raise MissingParameter('Missing parameter "id".')
        if not isinstance(id, int):
            raise TypeError('The parameter "int" must be integer.')

        request = self.__manager.request('get', self.__urls.get('all'))
        response = await request
        for element in response:
            if element['id'] == id:
                element['site_url'] = f"https://discordemoji.com/emoji/{element['slug']}"
                return APIResponse(element, 'get')
        return None

    async def packs(self):
        request = self.__manager.request('get', self.__urls.get('packs'))
        response = await request
        response.sort(key=lambda d: d['id'])
        packs = []
        for pack in response:
            pack['site_url'] = f"https://discordemoji.com/pack/{pack['slug']}"
            packs.append(pack)
        return packs

    async def stats(self):
        request = self.__manager.request('get', self.__urls.get('stats'))
        response = await request
        return APIResponse(response, 'stats')
