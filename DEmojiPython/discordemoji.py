import requests
import json


from .errors import *


class GetMethod(object):
    def __init__(self):
        self.methods = {
            "total": "https://discordemoji.com/api",
            "packs": "https://discordemoji.com/api/packs",
            "categories": "https://discordemoji.com/api?request=categories",
            "stats": "https://discordemoji.com/api?request=stats"
        }

    def get_type(self, method):
        try:
            resp = requests.get(self.methods.get(method)).json()
        except json.decoder.JSONDecodeError:
            pass
        else:
            if resp is not None:
                return resp


class DiscordEmoji(object):

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
            res = list(GetMethod().get_type('total'))
            search = author
            emojisbyauthor = []
            for obj in res:
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
            res = list(GetMethod().get_type('total'))
            search = name
            if any([obj['title'] == search for obj in res]):
                def srt(obj: dict):
                    return obj['title'] == search
                res.sort(key=srt, reverse=True)
                return res[0]
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

    @staticmethod
    def packs():
        """
        Fetch DE emoji packs

        Returns
        -------
        list[dict]
            list of dict containing DE packs's info
        """
        res = GetMethod().get_type('packs')
        return res


DEmoji = DiscordEmoji()
