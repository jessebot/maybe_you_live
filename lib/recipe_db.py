#!/usr/bin/python
# MySQL querying and updates for a recipe site
# By Jesse Hunt
import sys
import MySQLdb
import yaml


def get_database_variable(global_variable):
    """ gets global variable given string variable name"""
    with open('../.config/database_config.yaml', 'r') as f:
        doc = yaml.load(f)
    txt = doc[global_variable]
    return txt


class recipeDatabaseJunk():
    """Class to do all the database lifting on maybeyou.live"""

    # grab all the yaml info

    db_host = get_database_variable("db_host")
    db_user = get_database_variable("db_user")
    db_pass = get_database_variable("db_pass")
    db_name = get_database_variable("db_name")

    db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_pass,
                         db=db_name)
    cur = db.cursor()

    def destroy(self,):
        """close database connection"""
        self.db.close()

    def get_recipes(self, name=None, restrictions=None):
        """go get the recipes, probably for the front page"""
        if not name and not restrictions:
            self.cur.execute("SELECT * FROM recipes")
            # print all the first cell of all the rows
            for row in self.cur.fetchall():
                print row
        else:
            q = "SELECT * FROM recipes where name='{0}'".format(name)
            self.cur.execute(q)
            # print all the first cell of all the rows
            for row in self.cur.fetchall():
                print row

    def insert_new_recipe(self, name, cuisine, prep_time, meal_type,
                          pre_vs_post, points_dict, macros_dict):
        """Takes recipe info, inserts to database"""
        q = ("""INSERT into recipes VALUES (0, {0}, 0, {1}, {2}, {3}, """ +
             """{4}, {5}, {6});""").format(name, cuisine, prep_time,
                                           meal_type, pre_vs_post,
                                           points_dict, macros_dict)
        self.cur.execute(q)

if __name__ == "__main__":
    help = 'A script that lets you query/update a recipe databse'
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

    database = recipeDatabaseJunk()

    if input_dict:
        database.insert_new_recipe(name, cuisine, prep_time, meal_type,
                                   pre_vs_post, points_dict, macros_dict)

    if query:
        if name:
            database.get_recipes(name)
        else:
            database.get_recipes()

    database.destroy()

    print "ALL DONE"
