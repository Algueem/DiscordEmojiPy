import aiohttp
import json
from asgiref.sync import async_to_sync


from .errors import *


class GetMethod(object):
    def __init__(self):
        self.methods = {
            "total": "https://discordemoji.com/api",
            "packs": "https://discordemoji.com/api/packs",
            "categories": "https://discordemoji.com/api?request=categories",
            "stats": "https://discordemoji.com/api?request=stats"
        }

    @async_to_sync
    async def get_type(self, method):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.methods.get(method)) as req:
                    resp = await req.json()
        except json.decoder.JSONDecodeError:
            pass
        else:
            if resp is not None:
                return resp


class DiscordEmoji(object):
    # Searchs

    @staticmethod
    def search_emojis(search: str = None):
        """
        Search DE emojis

        Parameters
        -------
        search: str, the name of the emoji you want to search

        Returns
        -------
        list[dict]
            list of dict containing emojis's info
        """
        if search:
            res = list(GetMethod().get_type('total'))
            emojis = []
            for obj in res:
                if search.lower() in obj['title'].lower():
                    emojis.append(obj)
            if len(emojis) > 0:
                return emojis
            elif len(emojis) <= 0:
                return None
        else:
            raise MissingParameter('Parameter search not specified')

    @staticmethod
    def search_by_author(author: str=None):
        """
        Fetch DE Emojis submitted by an user

        Parameters
        -------
        author: str, the user that you want to see the emojis sent by him
            name must be case-sensitive

        Returns
        -------
        list[dict]
            list with dicts containing the emojis's information
        """
        if author:
            res = GetMethod().get_type('total')
            emojis = list(res)
            search = author
            emojisbyauthor = []
            for obj in emojis:
                if obj['submitted_by'] == search:
                    emojisbyauthor.append(obj)
            if len(emojisbyauthor) > 0:
                return emojisbyauthor
            elif len(emojisbyauthor) <= 0:
                return None
        else:
            raise MissingParameter('Parameter author not specified')

    @staticmethod
    def search_by_name(name: str=None):
        """
        Fetch DE Emoji by name

        Parameters
        -------
        name: str, the emoji name
            name must be case-sensitive

        Returns
        -------
        dict
            dict containing the emojis's information
        """
        if name:
            emojis = list(GetMethod().get_type('total'))
            search = name
            if any([obj['title'] == search for obj in emojis]):
                def srt(obj: dict):
                    return obj['title'] == search
                emojis.sort(key=srt, reverse=True)
                return emojis[0]
            else:
                return None
        else:
            raise MissingParameter('Parameter name not specified')

    @staticmethod
    def search_by_id(emojiid: int=None):
        """
        Fetch DE Emoji by id

        Parameters
        -------
        emojiid: int, the emoji id in discordemoji

        Returns
        -------
        dict
            dict containing the emojis's information
        """
        if emojiid:
            res = list(GetMethod().get_type('total'))
            if any([obj['id'] == emojiid for obj in res]):
                def srt(obj: dict):
                    return obj['id'] == emojiid
                res.sort(key=srt, reverse=True)
                return res[0]
            else:
                return None
        else:
            raise MissingParameter('Parameter id not specified')

    # Info

    @staticmethod
    def stats():
        """
        Fetch DE stats

        Returns
        -------
        dict
            data given from the JSON response
        """
        res = GetMethod().get_type('stats')
        return res

    @staticmethod
    def packs():
        """
        Fetch DE emoji packs

        Returns
        -------
        list[dict]
            list of dict containing DE packs's info
        """
        res = list(GetMethod().get_type('packs'))
        res.sort(key=lambda d: d['id'])
        return res


DEmoji = DiscordEmoji()
