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
    print text
