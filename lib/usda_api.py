#!/usr/bin/python
# usda API script by jesse to add stuff to maybeyoulive
import json
import requests
import yaml


def get_usda_key():
    """ gets global variable given string variable name"""
    with open('../.config/usda_api_config.yaml', 'r') as f:
        doc = yaml.load(f)
    api_key = doc["api_key"]
    return api_key

class pull_nutritional_data():
    # grab custom USDA issued API key
    usda_key = get_usda_key()

    def get_food_report(self,):
        # bother the USDA. They're not doing anything important anyway...
        d_str = "&".join(['format=json', 'type=f', 'ndbno=' + '01009',
                             'api_key=' + usda_key])
        r = requests.get('http://api.nal.usda.gov/usda/ndb/reports/?' + d_str)
        r.json()
        print r.json()

    def get_food_report(self,):
        # bother the USDA. They're not doing anything important anyway...
        d_str = "&".join(['format=json', 'type=f', 'ndbno=' + '01009',
                             'api_key=' + usda_key])
        r = requests.get('http://api.nal.usda.gov/usda/ndb/reports/?' + d_str)
        r.json()
        print r.json()


if __name__ == "__main__":
    print "boop"
