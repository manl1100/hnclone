import logging
import time

import hackernews
from tornado import ioloop, web

log = logging.getLogger(__name__)

log.setLevel(logging.INFO)


class TopStoriesHandler(web.RequestHandler):

    async def get(self):
        item_ids = await hackernews.get_item_ids()
        topstories = await hackernews.get_items(item_ids)
        return self.write(dict(stories=topstories))

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header(
            'Access-Control-Allow-Methods', ' PUT, DELETE, OPTIONS'
        )

    def options(self):
        self.set_status(204)
        self.finish()


def make_app():
    return web.Application([
        (r"/stories", TopStoriesHandler),
    ], debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    ioloop.IOLoop.current().start()
