#coding=utf-8
import os
from tornado import ioloop,web



class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("index.html")

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "debug" : True
}

application = web.Application([
    (r'/', IndexHandler),
    (r'/index', IndexHandler)
],**settings)

if __name__ == "__main__":
    application.listen(9999)
    ioloop.IOLoop.instance().start()
