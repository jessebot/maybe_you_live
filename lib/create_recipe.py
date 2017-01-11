#!/usr/bin/python
# script by jesse to add stuff to maybeyoulive
import argparse
import logging
from recipe_db import recipeDatabaseJunk

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logging.info("Maybeyou.live core script: logging config loaded")


if __name__ == "__main__":
    help = 'A script that lets you query/update a recipe database'
    parser = argparse.ArgumentParser(description=help)
    parser.add_argument('--input', '-i', action='store_true', default=False,
                        help='provided you are inputting information')
    parser.add_argument('--query', '-q', action='store_true', default=False,
                        help='query the database for a reciepe(s). Will ' +
                             'return all if you do not specify other options.')
    parser.add_argument('--name', '-n', help='recipe name to query',
                        type=str, default=None)
    parser.add_argument('--cuisine', '-c', help='recipe cuisine to query',
                        type=str, default=None)
    parser.add_argument('--meal_type', '-m', help='recipe meal_type to query',
                        type=str, default=None)
    parser.add_argument('--prep_time', '-p', help='recipe prep_time to query',
                        type=str, default=None)

    args = parser.parse_args()

    input_dict = args.input
    query = args.query
    name = args.name
    meal_type = args.meal_type
    cuisine = args.cuisine
    prep_time = args.prep_time

    # open connection to MySQL
    database = recipeDatabaseJunk()

    # if we're adding a brand new recipe
    if input_dict:
        database.insert_new_recipe(name, cuisine, prep_time, meal_type,
                                   pre_vs_post, points_dict, macros_dict)

    # if we're just searching!
    if query:
    #    if any(name, meal_type, cuisine, prep_time, pre_vs_post, macros_dict):
    #       database.get_recipes(name, meal_type, cuisine)
    #  else:
        database.get_recipes()

    # must clean up database connection lest we wreck ourselves <3
    database.destroy()

    print "ALL DONE"
