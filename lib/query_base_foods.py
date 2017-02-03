#!/usr/bin/python
# only tested with Python 2.7.12
# script to query base foods
from myll_db import recipeDatabase
from usda_api import pull_nutritional_data


if __name__ == "__main__":

    # initialize the nutritional data API
    usda_ndb = pull_nutritional_data()

    # initial the database data we already have...
    database = recipeDatabase("../.config/database_config.yaml")
    # food_list = database.get_all_foods()
    some_food = raw_input("food please: ")
    nutritional_db_no, name = usda_ndb.get_food_ndbno(some_food, "a")

    # grab current data from USDA API

    # base macros
    base_food_dict = usda_ndb.get_food_report(nutritional_db_no)
    calories = base_food_dict["calories"].replace("kcal", "")
    protein = base_food_dict["protein"]
    carbs = base_food_dict["carbs"]
    sugar = base_food_dict["sugar"]
    fiber = base_food_dict["fiber"]
    lipids = base_food_dict["lipids"]
    
    # other known measurements
    measures_dicts = usda_ndb.get_food_measurements(nutritional_db_no)

    final_measurements = []
    for measure_dict in measures_dicts:
        small_list = []
        small_list.append(measure_dict['label'].replace('"',' inches'))
        small_list.append(measure_dict['eqv'])
        final_measurements.append(small_list)

    # fix the database
    database.insert_food(nutritional_db_no, name, calories, carbs, protein,
                         sugar, lipids, fiber, final_measurements)
    database.destroy()
