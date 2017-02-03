#!/usr/bin/python
# only tested with Python 2.7.12
# script to refresh a list of base foods every night
from recipe_db import recipeDatabase
from usda_api import pull_nutritional_data
import json
import requests
import yaml


if __name__ == "__main__":

    # initialize the nutritional data API
    usda_ndb = pull_nutritional_data()

    # initial the database data we already have...
    database = recipeDatabase("../.config/database_config.yaml")
    food_list = database.get_all_foods()

    # generate a list of usda nutirional database number IDs
    for nutritional_db_no in food_list:
        # grab current data
        base_food_dict = usda_ndb.get_food_report(nutritional_db_no)
        calories = base_food_dict["calories"]
        protein = base_food_dict["protein"]
        carbs = base_food_dict["carbs"]
        sugar = base_food_dict["sugar"]
        fiber = base_food_dict["fiber"]
        lipids = base_food_dict["lipids"]

        # other known measurements
        print " Here's all known measurements of this food ".center(80, "*")
        measures_dicts = usda_ndb.get_food_measurements(nutritional_db_no)
        for measure_dict in measures_dicts:
            print "label: ", measure_dict['label']
            print "amount in this measurment: ", measure_dict['eqv'], "g\n"
