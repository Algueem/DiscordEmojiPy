from .errors import InvalidAttribute

class APIResponse:
    def __init__(self, obj, typeobj):
        self.__obj = None
        self.__stats = None
        if typeobj == 'get':
            self.__obj = obj
        elif typeobj == 'stats':
            self.__stats = obj
        else:
            pass

    # --- GET--- #

    @property
    def dict(self):
        if self.__obj:
            return self.__obj
        elif self.__stats:
            return self.__stats

    @property
    def name(self):
        if self.__obj:
            return self.__obj['title']
        else:
            raise InvalidAttribute('This response have no attribute "name"')

    @property
    def id(self):
        if self.__obj:
            return self.__obj['id']
        else:
            raise InvalidAttribute('This response have no attribute "id"')

    @property
    def image_url(self):
        if self.__obj:
            return self.__obj['image']
        else:
            raise InvalidAttribute('This response have no attribute "image_url"')

    @property
    def description(self):
        if self.__obj:
            return self.__obj['description']
        else:
            raise InvalidAttribute('This response have no attribute "description"')

    @property
    def faves(self):
        if self.__obj:
            return self.__obj['faves']
        elif self.__stats:
            return self.__stats['faves']
        else:
            raise InvalidAttribute('This response have no attribute "faves"')

    @property
    def by(self):
        if self.__obj:
            return self.__obj['submitted_by']
        else:
            raise InvalidAttribute('This response have no attribute "by"')

    @property
    def slug(self):
        if self.__obj:
            return self.__obj['slug']
        else:
            raise InvalidAttribute('This response have no attribute "slug"')

    @property
    def site_url(self):
        if self.__obj:
            return self.__obj['site_url']
        else:
            raise InvalidAttribute('This response have no attribute "site_url"')

    # --- STATS --- #

    @property
    def count(self):
        if self.__stats:
            return self.__stats['emoji']
        else:
            raise InvalidAttribute('This response have no attribute "count"')

    @property
    def users(self):
        if self.__stats:
            return self.__stats['users']
        else:
            raise InvalidAttribute('This response have no attribute "users"')

    @property
    def pending(self):
        if self.__stats:
            return self.__stats['pending_approvals']
        else:
            raise InvalidAttribute('This response have no attribute "pending"')
