#!/usr/bin/python
# MySQL querying and updates for a recipe site
# By Jesse Hunt
import argparse
import sys
import MySQLdb
import yaml


def get_database_variable(yaml_file, global_variable):
    """ gets global variable given string variable name"""
    with open(yaml_file, 'r') as f:
        doc = yaml.load(f)
    txt = doc[global_variable]
    return txt


class recipeDatabase():
    """Class to do all the database lifting on maybeyou.live"""
    def __init__(self, yaml_file):
        # grab all the yaml info
    
        db_host = get_database_variable(yaml_file, "db_host")
        db_user = get_database_variable(yaml_file, "db_user")
        db_pass = get_database_variable(yaml_file, "db_pass")
        db_name = get_database_variable(yaml_file, "db_name")
    
        self.db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_pass,
                                  db=db_name)
        self.cur = self.db.cursor()

    def destroy(self,):
        """close database connection"""
        self.db.close()

    def get_recipes(self, name=None, restrictions=None):
        """go get the recipes, probably for the front page"""
        if not name and not restrictions:
            self.cur.execute("SELECT * FROM recipes")
        else:
            q = "SELECT * FROM recipes where name='{0}'".format(name)
            self.cur.execute(q)
        return self.cur.fetchall()

    def insert_new_recipe(self, name, cuisine, prep_time, meal_type,
                          pre_vs_post, points_dict, macros_dict):
        """Takes recipe info, inserts to database"""
        q = ("""INSERT into recipes VALUES (0, {0}, 0, {1}, {2}, {3}, """ +
             """{4}, {5}, {6});""").format(name, cuisine, prep_time,
                                           meal_type, pre_vs_post,
                                           points_dict, macros_dict)
        self.cur.execute(q)

if __name__ == "__main__":
    usage = 'Usage: recipe_db.py [-q/-i/-n] [<input>/<query>/<name>]'
    help = 'A script that lets you query/update a recipe database. ' + usage
    parser = argparse.ArgumentParser(description=help)
    parser.add_argument('--input', '-i', action='store_true', default=False,
                        help='This has to be a dictionary of information ' +
                             'about the recipe: name, cuisine, prep_time' +
                             ', meal_type')
    parser.add_argument('--query', '-q', action='store_true', default=False,
                        help='query the database for a reciepe(s). Will ' +
                             'return all if you do not specify other options.')
    parser.add_argument('--name', '-n', help='recipe name to query',
                        default=None)

    args = parser.parse_args()


    input_dict = args.input
    query = args.query
    name = args.name

    if not args.input and not args.query:
        print usage

    database = recipeDatabase("../.config/database_config.yaml")

    if input_dict:
        database.insert_new_recipe(name, cuisine, prep_time, meal_type,
                                   pre_vs_post, points_dict, macros_dict)

    if query:
        if name:
            for row in database.get_recipes(name):
                print row
        else:
            for row in database.get_recipes():
                print row

    database.destroy()
