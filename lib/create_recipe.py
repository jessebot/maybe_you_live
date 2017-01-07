#!/usr/bin/python
# script by jesse to add stuff to maybeyoulive
import argparse
import logging
from recipe_db import recipeDatabaseJunk

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logging.info("Maybeyou.live core script: logging config loaded")


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
