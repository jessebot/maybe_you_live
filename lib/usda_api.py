#!/usr/bin/python
# usda API script and libraries by jessebot to add stuff to maybeyou.live
# only tested with Python 2.7.12
from collections import OrderedDict
import json
import requests
import yaml


def get_usda_key():
    """
    Gets global variable given string variable name
    """
    with open('../.config/usda_api_config.yaml', 'r') as f:
        doc = yaml.load(f)
    api_key = doc["api_key"]
    return api_key


class pull_nutritional_data():
    """
    Bother the USDA. They're not doing anything important anyway...
    """

    # grab custom USDA issued API key
    usda_key = get_usda_key()

    def get_food_ndbno(self, food_str, food_group_str=None):
        # base keys we have to pass in
        keys = ["format=json", "q=" + food_str, "max=25", "offset=0"]

        # if they want to be granular about their search...
        if food_group_str:
            group = food_group_str.replace(" ", "%20")
            keys.append("fg=" + group)

        # the API key wold be helpful...
        keys.append("api_key=" + self.usda_key)

        # create a stellar URL
        data = "&".join(keys)

        # bother the USDA. They're not doing anything important anyway...
        resp = requests.get('http://api.nal.usda.gov/usda/ndb/search/?' + data)
        report_dict = json.loads(resp.text)['list']
        return report_dict['item'][0]['ndbno']

    def get_food_report(self, usda_id):
        """
        Core function of class, Queries API directly.
        """

        data = "&".join(['format=json', 'type=f', 'ndbno=' + usda_id,
                         'api_key=' + self.usda_key])
        resp = requests.get('http://api.nal.usda.gov/usda/ndb/reports/?' +
                            data)
        # you start out with a giant "report"
        report_dict = json.loads(resp.text)['report']
        # the most needless content wrapper...
        food_dict = report_dict['food']

        # there we freakin' go~! The data we actually care about <3
        nutrients = food_dict['nutrients']
        r_dict = {}

        # add the calories
        r_dict['calories'] = str(nutrients[1]['value']) + nutrients[1]['unit']

        # add the protein
        r_dict['protein'] = str(nutrients[3]['value']) + nutrients[3]['unit']

        # add the lipids
        r_dict['lipids'] = str(nutrients[4]['value']) + nutrients[4]['unit']

        # add the carbs
        r_dict['carbs'] = str(nutrients[6]['value']) + nutrients[6]['unit']

        # add the fiber
        r_dict['fiber'] = str(nutrients[7]['value']) + nutrients[7]['unit']

        # add the sugar
        r_dict['sugar'] = str(nutrients[8]['value']) + nutrients[8]['unit']

        # add the calcium
        r_dict['calcium'] = str(nutrients[16]['value']) + nutrients[16]['unit']

        # add the iron
        r_dict['iron'] = str(nutrients[17]['value']) + nutrients[17]['unit']

        # add the magnesium
        r_dict['magnesium'] = str(nutrients[18]['value']) + nutrients[18]['unit']

        # add the phosphorus
        r_dict['phosphorus'] = str(nutrients[19]['value']) + nutrients[19]['unit']

        # add the potassium
        r_dict['potassium'] = str(nutrients[20]['value']) + nutrients[20]['unit']

        # add the sodium
        r_dict['sodium'] = str(nutrients[21]['value']) + nutrients[21]['unit']

        # add the zinc
        r_dict['zinc'] = str(nutrients[22]['value']) + nutrients[22]['unit']

        # add the copper
        r_dict['copper'] = str(nutrients[23]['value']) + nutrients[23]['unit']

        # add the Manganese
        r_dict['manganese'] = str(nutrients[24]['value']) + nutrients[24]['unit']

        # add the selenium
        r_dict['selenium'] = str(nutrients[25]['value']) + nutrients[25]['unit']

        # add the fluoride
        r_dict['fluoride'] = str(nutrients[26]['value']) + nutrients[26]['unit']

        # add the vitamin c
        r_dict['vitamin_c'] = str(nutrients[27]['value']) + nutrients[27]['unit']

        # add the thiamin
        r_dict['thiamin'] = str(nutrients[28]['value']) + nutrients[28]['unit']

        # add the riboflavin
        r_dict['riboflavin'] = str(nutrients[29]['value']) + nutrients[29]['unit']

        # add the niacin
        r_dict['niacin'] = str(nutrients[30]['value']) + nutrients[30]['unit']

        # add the vitamin b-6
        r_dict['vitamin_b-6'] = str(nutrients[32]['value']) + nutrients[32]['unit']

        # add the folate
        r_dict['folate'] = str(nutrients[33]['value']) + nutrients[33]['unit']

        # add the choline
        r_dict['choline'] = str(nutrients[37]['value']) + nutrients[37]['unit']

        # add the betaine
        r_dict['betaine'] = str(nutrients[38]['value']) + nutrients[38]['unit']

        # add the vitamin_b-12
        r_dict['vitamin_b-12'] = str(nutrients[39]['value']) + nutrients[39]['unit']

        # add the vitamin_a-rae
        r_dict['vitamin_a-rae'] = str(nutrients[41]['value']) + nutrients[41]['unit']

        # add the retinol
        r_dict['retinol'] = str(nutrients[42]['value']) + nutrients[42]['unit']

        # add the carotene_beta
        r_dict['carotene_beta'] = str(nutrients[43]['value']) + nutrients[43]['unit']

        # add the carotene_alpha
        r_dict['carotene_alpha'] = str(nutrients[44]['value']) + nutrients[44]['unit']

        # add the vitamin_a-iu
        r_dict['vitamin_a-iu'] = str(nutrients[45]['value']) + nutrients[45]['unit']

        # add the vitamin_e
        r_dict['vitamin_e'] = str(nutrients[48]['value']) + nutrients[48]['unit']

        # add the vitamin_d2_d3
        r_dict['vitamin_d2-d3'] = str(nutrients[53]['value']) + nutrients[53]['unit']

        # add the vitamin_d
        r_dict['vitamin_d'] = str(nutrients[54]['value']) + nutrients[54]['unit']

        # add the vitamin_k
        r_dict['vitamin_k'] = str(nutrients[56]['value']) + nutrients[56]['unit']

        # add the saturated_fatty_acid
        r_dict['saturated_fat'] = str(nutrients[57]['value']) + nutrients[57]['unit']

        # add the monounsaturated_fatty_acid
        r_dict['monounsaturated_fat'] = str(nutrients[71]['value']) + nutrients[71]['unit']

        # add the polyunsaturated_fatty_acid
        r_dict['polyunsaturated_fat'] = str(nutrients[79]['value']) + nutrients[79]['unit']

        # add the trans_fatty_acid
        r_dict['trans_fat'] = str(nutrients[89]['value']) + nutrients[89]['unit']

        # add the cholesterol
        r_dict['cholesterol'] = str(nutrients[90]['value']) + nutrients[90]['unit']

        # all done!
        return r_dict

    def get_food_measurements(self, usda_id):
        """
        just kinds of measurements
        """

        data = "&".join(['format=json', 'type=f', 'ndbno=' + usda_id,
                         'api_key=' + self.usda_key])
        resp = requests.get('http://api.nal.usda.gov/usda/ndb/reports/?' + data)
        # you start out with a giant "report"
        report_dict = json.loads(resp.text)['report']
        # the most needless content wrapper...
        food_dict = report_dict['food']

        # there we freakin' go~! The data we actually care about <3
        nutrients = food_dict['nutrients']

        return nutrients[0]['measures']


if __name__ == "__main__":

    # initialize the nutritional data API
    usda_ndb = pull_nutritional_data()

    # prompt user for string of food they want...
    print('\nWelcome to the USDA Nutritional Database. I will be your guide' +
          '. This isn\'t going \nto be pretty, but we\'ll get the job done' +
          '. When asked, be specific about what you\nwant, so "raw carrot", ' +
          'instead of "carrot". It might still fail though...')

    some_food = raw_input("\nTell me what food you'd like to learn about: ")
    initial_fg_dict = {'1': 'Vegetables and Vegetable Products',
                       '2': 'Legumes and Legume Products',
                       '3': 'Nut and Seed Products',
                       '4': 'Fruits and Fruit Juices',
                       '5': 'Fats and Oils',
                       '6': 'Cereal Grains and Pasta',
                       '7': 'Spices and Herbs',
                       '8': 'Baked Products',
                       '9': 'Breakfast Cereals',
                       '10': 'Soups, Sauces, and Gravies',
                       '11': 'Dairy and Egg Products',
                       '12': 'Poultry Products',
                       '13': 'Beef Products',
                       '14': 'Pork Products',
                       '15': 'Lamb, Veal, and Game Products',
                       '16': 'Finfish and Shellfish Products',
                       '17': 'Sausages and Luncheon Meats',
                       '18': 'Beverages',
                       '19': 'American Indian/Alaska Native Foods',
                       '20': 'Meals, Entrees, and Side Dishes',
                       '21': 'Snacks',
                       '22': 'Sweets',
                       '23': 'Baby Foods',
                       '24': 'Branded Food Products Database'}
    fg_dict = OrderedDict(sorted(initial_fg_dict.items(), key=lambda t: t[0]))

    # make them select a category to filter results
    for key, value in fg_dict.iteritems():
        print key, ":", value
    some_kind = raw_input("\nType the number of the category you need: ")

    # try:
    # the first number we find
    nutritional_db_no = usda_ndb.get_food_ndbno(some_food,
                                                fg_dict.get(some_kind))
    print "\nWe pulled nutrition ID: ", nutritional_db_no, "\n"
    # all macros, some micros
    print " Here's just the nutritional data for 100g ".center(80, "*")
    base_food_dict = usda_ndb.get_food_report(nutritional_db_no)
    # except Exception as e:
    #     print("\nLol, so... shit's particularly kickass today, and there's " +
    #           "nothing I can do for you.\nSorry, scro.", e)
    # else:
    for key, value in base_food_dict.iteritems():
        print key, " : ", value

    # other known measurements
    print ""
    print " Here's all known measurements of this food ".center(80, "*")
    measures_dicts = usda_ndb.get_food_measurements(nutritional_db_no)
    for measure_dict in measures_dicts:
        print "label: ", measure_dict['label']
        print "amount in this measurment: ", measure_dict['eqv'], "g\n"
