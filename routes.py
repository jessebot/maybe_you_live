import os
from tornado import web, wsgi
import wsgiref.simple_server

# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello, world")

settings = {
    "static_path": "./static",
    "server_name": "maybeyou.live",
    "debug": True,
}

class MainHandler(web.RequestHandler):
    def get(self):
        self.render(settings['static_path'] + "/templates/index.html",
                    server_name=settings['server_name'])

if __name__ == "__main__":
    application = web.Application([
        (r"/", MainHandler),
        (r"/static/(.*)", web.StaticFileHandler,
         {"path": settings['static_path']}),
    ], **settings)
    wsgi_app = wsgi.WSGIAdapter(application)
    server = wsgiref.simple_server.make_server('', 8000, wsgi_app)
    server.serve_forever()
