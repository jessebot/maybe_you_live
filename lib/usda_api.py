#!/usr/bin/python
# usda API script by jesse to add stuff to maybeyoulive
import json
import pprint
import requests
from xml.etree import ElementTree
import yaml


def get_usda_key():
    """ gets global variable given string variable name"""
    with open('../.config/usda_api_config.yaml', 'r') as f:
        doc = yaml.load(f)
    api_key = doc["api_key"]
    return api_key

class pull_nutritional_data():
    """bother the USDA. They're not doing anything important anyway..."""

    # grab custom USDA issued API key
    usda_key = get_usda_key()

    def get_food_report(self, usda_id):
        data = "&".join(['format=json', 'type=f', 'ndbno=' + usda_id,
                         'api_key=' + self.usda_key])
        r = requests.get('http://api.nal.usda.gov/usda/ndb/reports/?' + data)
        # r.json()
        # print r.json()
        pprint.pprint(json.loads(r.text))

    def get_food_ndbno(self, food_str):
        # bother the USDA. They're not doing anything important anyway...
        data = "&".join(['format=json', 'q=' + food_str, 'max=25', 'offset=0',
                         'api_key=' + self.usda_key])
        r = requests.get('http://api.nal.usda.gov/usda/ndb/search/?' + data)
        r.json()
        print r.json()


if __name__ == "__main__":
    derp = pull_nutritional_data()
    print "here's us searching for 'raw carrot'"
    print derp.get_food_ndbno("raw carrot")
    print "here's us searching for the raw carrot's full food report"
    print derp.get_food_report("11124")
    print "fin!"
