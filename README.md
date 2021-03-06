# DiscordEmojiPy - DiscordEmoji API Wrapper for Python
## Documentation

### English

#### Installation

```
pip install demojipy
```


#### Search:
```python
import demoji

demojiclient = demoji.Client(use_cache=False)
demojiclient.attr()
```

Available attributes:  

Attribute | Parameters | Return | Description
-------- | -------- | -------- | --------
get_by_id() | id: int | APIResponse object | Fetch DiscordEmoji's Emoji by id
get_by_name() | name: str | APIResponse object | Fetch DiscordEmoji's Emoji by name
search_by_author() | author: str | list[dict] | Fetch DiscordEmoji's Emojis submitted by an user
get_emojis() | search: str, startswith: bool | list[dict] | Fetch emojis you want to search, specifying whether search will be by the beginning of the word (default) or not (by specifying False in the startswith parameter)
stats() | None | APIResponse object | Fetch DiscordEmoji's stats
packs() | None | list[dict] | Fetch DiscordEmoji's emoji packs

### Examples:
```python
from DEmojiPython import DEmoji
# Code
DEmoji.search_by_id(1)
# Response
{'id': 1, 'title': 'zombie', 'slug': 'zombie', 'image': 'https://discordemoji.com/assets/emoji/zombie.png', ...}

# Code
DEmoji.search_by_name('zombie') # must be case insensitive
# Response:
{'id': 1, 'title': 'zombie', 'slug': 'zombie', 'image': 'https://discordemoji.com/assets/emoji/zombie.png', ...}

# Code
DEmoji.search_by_author('Kohai') # must be case insensitive
# Response
[{'title': 'emoji', 'submitted_by': 'Kohai'},
{'title': 'emojiTwo', 'submitted_by': 'Kohai'}...]

# Code
DEmoji.search_emojis('PR_', startswith=True)
# Response
[{'id': 3830, 'title': 'PR_bug', ...}, ...]
# If not found, returns None


# Code
DEmoji.stats()
# Response:
{"emoji": int,"users": int,"faves": int,"pending_approvals": int}

# Code
DEmoji.packs()
#Response:
[{"id":2,"name":"Anime Pack  #1", ...}, ...]
```

More attributes are coming soon...

If there is any grammar error call me at Discord: Alguem#1599

## ChangeLog
### v3.0.0
- Async Request
- Added client
- Cache Setting
- Added APIResponse object

### v2.0.1
- Fix cache bug
### v2.0.0
- [X] Add site urls in dicts
- Change aiohttp to requests again(because very bugs)
- Added parameter "startswith" in "search_emojis"(specifies whether search will be by the beginning of the word or not)
- Added Packs attribute
- Added cache system, to avoid making too many requests for api.
### v2.0.0a
- Change requests to aiohttp(testing) 
- Added Packs attribute(Testing)

## Future Updates
- [ ] Add categories
