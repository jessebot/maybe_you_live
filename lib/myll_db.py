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
        q = ("SELECT id, name, calories, carbs, lipids, protein, sugar ")
        if not name and not restrictions:
            self.cur.execute(q + "FROM recipes")
        else:
            self.cur.execute(q + "FROM recipes where name='{0}'".format(name))

        # here's the return from the database
        tuple_o_recipes = self.cur.fetchall()

        final_list = []

        # formatting things much more nicely
        for row in tuple_o_recipes:
            new_dict = {}
            new_dict["id"] = row[0]
            new_dict["name"] = row[1]
            new_dict["calories"] = row[2]
            new_dict["carbs"] = row[3]
            new_dict["lipids"] = row[4]
            new_dict["protein"] = row[5]
            new_dict["sugar"] = row[6]
            final_list.append(new_dict)

        return final_list

    def insert_new_recipe(self, name, cuisine, prep_time, meal_type,
                          pre_vs_post, points_dict, macros_dict):
        """Takes recipe info, inserts to database"""
        q = ("""INSERT into recipes VALUES (0, {0}, 0, {1}, {2}, {3}, """ +
             """{4}, {5}, {6});""").format(name, cuisine, prep_time,
                                           meal_type, pre_vs_post,
                                           points_dict, macros_dict)
        self.cur.execute(q)

    def get_food(self, name=None):
        """go get the base food and info about it"""
        q = ("SELECT ndbno, name, calories, carbs, lipids, protein, sugar ")
        self.cur.execute(q + "FROM base_foods where name='{0}'".format(name))

        # here's the return from the database
        tuple_o_foods = self.cur.fetchall()

        final_list = []

        # formatting things much more nicely
        for row in tuple_o_foods:
            new_dict = {}
            new_dict["ndbno"] = row[0]
            new_dict["name"] = row[1]
            new_dict["calories"] = row[2]
            new_dict["carbs"] = row[3]
            new_dict["lipids"] = row[4]
            new_dict["protein"] = row[5]
            new_dict["sugar"] = row[6]
            final_list.append(new_dict)

        return final_list

    def get_all_foods(self):
        """go get the base foods by their ndbno"""
        self.cur.execute("SELECT ndbno FROM base_foods")

        # here's the return from the database
        food_ids = self.cur.fetchall()

        final_list = []

        # formatting things much more nicely
        for row in food_ids:
            final_list.append(str(row[0]))

        return final_list

    def update_food(self, ndbno, calories, carbs, protein, sugar, lipids,
                    fiber, measurements):
        """go update the base foods by their ndbno"""

        # formatting things much more nicely
        q = ('''update base_foods set calories="{0}", carbs="{1}",''' +
             '''protein="{2}", sugar="{3}", lipids="{4}", fiber="{5}", ''' +
             '''measurements="{6}" where ''' +
             '''ndbno="{7}"''').format(calories, carbs, protein, sugar,
                                       lipids, fiber, measurements, ndbno)
        self.cur.execute(q)

    def insert_food(self, ndbno, name, calories, carbs, protein, sugar,
                    lipids, fiber, measurements):
        """Takes food info, inserts to database"""
        q = ("""INSERT into base_foods VALUES""" +
             """("{0}", "{1}", "{2}", "{3}", "{4}", "{5}", "{6}",""" +
             """"{7}", "{8}")""").format(ndbno, name, calories, carbs, protein,
                                         sugar, lipids, fiber, measurements)
        self.cur.execute(q)


if __name__ == "__main__":
    usage = 'Usage: myll_db.py [-q/-i/-n] [<input>/<query>/<name>]'
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
            recipe_list = database.get_recipes(name)
            for row in recipe_list:
                print row
        else:
            recipe_list = database.get_recipes()
            for row in recipe_list:
                print row

    database.destroy()
