#!/usr/bin/python
# Jesse's recipe conversion thingy, woo!
from textract import process
import os

list_o_files = []

for dir_path, dir_names, file_names in os.walk("./static/documents"):
    list_o_files.extend(file_names)
    break

for recipe in list_o_files:
    text = process("./static/documents/" + recipe)
    r_txt_name = recipe.replace('pdf','txt')
    r_name = r_txt_name.replace('-', '_').replace('___', '_').replace('__', '_')
    with open("./static/recipes/" + r_name, 'w') as recipe_file:
        recipe_file.write(text)
