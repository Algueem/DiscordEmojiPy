import requests
import json
from datetime import datetime, timedelta
import os

from .errors import *


class GetMethod(object):
    def __init__(self, method):
        self.methods = {
            "total": "https://discordemoji.com/api",
            "packs": "https://discordemoji.com/api/packs",
            "categories": "https://discordemoji.com/api?request=categories",
            "stats": "https://discordemoji.com/api?request=stats"
        }
        self.method = method

    def get(self):
        import DEmojiPython
        path = DEmojiPython.__path__[0]
        if not os.path.exists(path + '/cache.json'):
            open(path + '/cache.json', 'w')
            with open(path + '/cache.json', 'w') as fp:
                obj = {}
                json.dump(obj=obj, fp=fp, indent=4)
        cache = json.load(open(path + '/cache.json', 'r'))
        met = cache.get(self.method)
        if met:
            if self.method in ('total', 'stats'):
                if datetime.utcnow() <= datetime.strptime(cache[self.method]['request_after'], "%Y-%m-%d %H:%M:%S.%f"):
                    return cache[self.method]['info']
                else:
                    pass
            else:
                return cache[self.method]['info']
        req = requests.get(self.methods.get(self.method))
        try:
            response = req.json()
        except json.JSONDecodeError:
            raise RequestFailed("Can't make request to API. Try again later.")
        else:
            cache[self.method] = {}
            cache[self.method]['info'] = response
            if self.method in ('total', 'stats'):
                cache[self.method]['request_after'] = f'{datetime.utcnow() + timedelta(minutes=30)}'
            with open(path + '/cache.json', 'w') as fp:
                json.dump(cache, fp, indent=4)
            return response



class DiscordEmoji(object):
    # Searchs
    @staticmethod
    def search_emojis(search: str = None, startswith: bool=True):
        """
        Search DE emojis

        Parameters
        -------
        search: str, the name of the emoji you want to search

        startswith: bool, specifies whether search will be by the beginning of the word or not

        Returns
        -------
        list[dict]
            list of dict containing emojis's info
        """
        if search:
            res = GetMethod('total').get()
            emojis = []
            for obj in res:
                if startswith:
                    if obj['title'].lower().startswith(search.lower()):
                        obj['site_url'] = f"https://discordemoji.com/emoji/{obj['slug']}"
                        emojis.append(obj)
                else:
                    if search.lower() in obj['title'].lower():
                        obj['site_url'] = f"https://discordemoji.com/emoji/{obj['slug']}"
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
            emojis = GetMethod('total').get()
            search = author
            emojisbyauthor = []
            for obj in emojis:
                if obj['submitted_by'] == search:
                    obj['site_url'] = f"https://discordemoji.com/emoji/{obj['slug']}"
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
            emojis = GetMethod('total').get()
            search = name
            if any([obj['title'] == search for obj in emojis]):
                def srt(obj: dict):
                    return obj['title'] == search
                emojis.sort(key=srt, reverse=True)
                emoji = emojis[0]
                emoji['site_url'] = f"https://discordemoji.com/emoji/{emoji['slug']}"
                return emoji
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
            emojis = GetMethod('total').get()
            if any([obj['id'] == emojiid for obj in emojis]):
                def srt(obj: dict):
                    return obj['id'] == emojiid
                emojis.sort(key=srt, reverse=True)
                emoji = emojis[0]
                emoji['site_url'] = f"https://discordemoji.com/emoji/{emoji['slug']}"
                return emoji
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
        res = GetMethod('stats').get()
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
        packsreq = GetMethod('packs').get()
        packsreq.sort(key=lambda d: d['id'])
        packs = []
        for pack in packsreq:
            pack['site_url'] = f"https://discordemoji.com/pack/{pack['slug']}"
            packs.append(pack)

        return packs


DEmoji = DiscordEmoji()
