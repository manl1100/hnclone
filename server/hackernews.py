import json
import logging

from tornado import gen, httpclient

from cache import memoize

log = logging.getLogger(__name__)

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{item_id}.json"

client = httpclient.AsyncHTTPClient()


async def get_item_ids():
    response = await client.fetch(TOP_STORIES_URL)
    return response.body[:10]


@memoize(ttl=5)
async def get_items(item_ids):
    topstories = []
    futures = [
        client.fetch(ITEM_URL.format(item_id=id))
        for id in item_ids
    ]

    async for response in gen.WaitIterator(*futures):
        item = json.loads(response.body)
        if item["type"] != "story":
            continue
        topstories.append(item)

    return topstories
