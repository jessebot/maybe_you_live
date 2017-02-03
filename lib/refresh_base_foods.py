#!/usr/bin/python
# usda API script and libraries by jessebot to add stuff to maybeyou.live
# only tested with Python 2.7.12
from collections import OrderedDict
from usda_api import *
import json
import requests
import yaml


if __name__ == "__main__":

    # initialize the nutritional data API
    usda_ndb = pull_nutritional_data()

    recipething = nutritional_db_no
    try:
        # all macros, some micros
        print " Here's just the nutritional data for 100g ".center(80, "*")
        base_food_dict = usda_ndb.get_food_report(nutritional_db_no)
    except Exception as e:
        print("\nLol, so... shit's particularly kickass today, and there's " +
              "nothing I can do for you.\nSorry, scro.")
    else:
        for key, value in base_food_dict.iteritems():
            print key, " : ", value

        # other known measurements
        print ""
        print " Here's all known measurements of this food ".center(80, "*")
        measures_dicts = usda_ndb.get_food_measurements(nutritional_db_no)
        for measure_dict in measures_dicts:
            print "label: ", measure_dict['label']
            print "amount in this measurment: ", measure_dict['eqv'], "g\n"
