# Jesse's tornado + polymer mess
import os
from tornado import web, wsgi
import sys
import wsgiref.simple_server

settings = {
    "static_path": "./static",
    "app_name": "Maybe You Live",
    "debug": True,
}

class MainHandler(web.RequestHandler):
    def get(self):
        self.render(settings['static_path'] + "/templates/index.html",
                    app_name=settings['app_name'])

if __name__ == "__main__":
    application = web.Application([
        (r"/", MainHandler),
        (r"/submit", MainHandler),
        (r"/start", MainHandler),
        (r"/about", MainHandler),
        (r"/static/(.*)",
         web.StaticFileHandler, {"path": settings['static_path']})
    ], **settings)
    wsgi_app = wsgi.WSGIAdapter(application)
    server = wsgiref.simple_server.make_server('', 8000, wsgi_app)
    server.serve_forever()
