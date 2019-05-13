# Docs | DiscordEmojiPy - DiscordEmoji API Wrapper for Python

## EN Docs

### Installation

```
pip install demojipy
```


### Search:
```python
from DEmojiPython import DEmoji

DEmoji.attr
```

Available attributes:  

Attribute | Parameters | Return | Description
-------- | -------- | -------- | --------
search_by_id() | emojiid: int | dict | Fetch DiscordEmoji's Emoji by id
search_by_name() | name: str | dict | Fetch DiscordEmoji's Emoji by name
search_by_author() | author: str | list[dict] | Fetch DiscordEmoji's Emojis submitted by an user
stats() | None | dict | Fetch DiscordEmoji's stats

### Examples:
```python
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

# If not found, returns None


# Code
DEmoji.stats()
# Response:
{"emoji":int,"users":int,"faves":int,"pending_approvals":int}
```


More attributes are coming soon...
If there is any grammar error call me at Discord: Alguem#7724
