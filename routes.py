#!/usr/bin/python
# Jesse Hitch's recipe website <3 
# 2/3/17
import json
import sys
sys.path.append('./lib')
from myll_db import recipeDatabase
from tornado import web, wsgi
import tornado.escape
import tornado.ioloop
import tornado.web
import wsgiref.simple_server

settings = {"static_path": "./static",
            "app_name": "Maybe You Live",
            "debug": True}


class MainHandler(web.RequestHandler):
    def get(self):
        self.render(settings['static_path'] + "/templates/index.html",
                    app_name=settings['app_name'])

class VersionHandler(web.RequestHandler):
    def get(self):
        response = { 'version': '.5'}
        self.write(response)
 
class GetRecipeByIdHandler(web.RequestHandler):
    def get(self, id):
        response = { 'id': int(id),
                     'name': 'ON NOM NOM'}
        self.write(response)

class GetAllRecipes(web.RequestHandler):
    def get(self):
        database = recipeDatabase("./.config/database_config.yaml")
        recipe_list = database.get_recipes()
        self.write(json.dumps(recipe_list))
 
if __name__ == "__main__":
    application = web.Application([(r"/", MainHandler),
                                   (r"/submit", MainHandler),
                                   (r"/start", MainHandler),
                                   (r"/check", MainHandler),
                                   (r"/about", MainHandler),
                                   (r"/getallrecipes", GetAllRecipes),
                                   (r"/getrecipebyid/([0-9]+)",
                                       GetRecipeByIdHandler),
                                   (r"/version", VersionHandler),
                                   (r"/static/(.*)", web.StaticFileHandler,
                                    {"path": settings['static_path']})
                                   ], **settings)
    wsgi_app = wsgi.WSGIAdapter(application)
    server = wsgiref.simple_server.make_server('', 8000, wsgi_app)
    server.serve_forever()
