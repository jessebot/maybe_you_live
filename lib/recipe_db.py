#!/usr/bin/python
# MySQL querying and updates for a recipe site
# By Jesse Hunt
import argparse
import logging
import sys
import MySQLdb
# import yaml

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logging.info("Maybeyou.live database libs: logging config loaded")

class recipeDatabaseJunk():
    # db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_pass,
    #                      db=database)
    cur = db.cursor()

    def destroy(self,):
        """close database connection"""
        db.close()
    
    def get_recipes(self, restrictions=None):
        """go get the recipes, probably for the front page"""
        self.cur.execute("SELECT * FROM recipes")
        # print all the first cell of all the rows
        for row in self.cur.fetchall():
            print row[0]

    def insert_new_recipe(self, name, cuisine, prep_time, meal_type,
                          pre_vs_post, points_dict, macros_dict):
        """Takes recipe info, inserts to database"""
         q = ("""INSERT into recipes VALUES (0, {0}, 0, {1}, {2}, {3}, """ +
              """{4}, {5}, {6});""").format(name, cuisine, prep_time,
                                            meal_type, pre_vs_post,
                                            points_dict, macros_dict)
         self.cur.execute(q)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=('A script that lets you query/update a recipe databse ' +
                     'and its nutritional information')
    parser.add_argument('--input', '-i',
                        help='This has to be a dictionary of information ' +
                              'about the recipe: name, cuisine, prep_time, ' +
                              'meal_type')
    parser.add_argument('--query', '-q',
                        help='query the database for a reciepe(s). Will ' +
                             'return all if you do not specify other options.')
    parser.add_argument('--name', '-n', help='recipe name to query')

    args = parser.parse_args()

    input_dict = args.input
    query = args.query
    name = args.name

    database = recipeDatabaseJunk()
