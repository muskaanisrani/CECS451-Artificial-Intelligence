"""
Read a csv file into a tree and its values into dictionary

Date: August 4th, 2021
Authors: Keval Varia
Student ID: 017834282, 017537908
Class: CECS 451- Artificial Intelligence
"""

import csv
from Tree import *


def readFile(tree, input_file):
    # variable declaration
    obtained_inputs = {}
    possible_outcomes = ["A", "B", "C", "D", "E", "F",
                         "G", "H", "I", "J", "K", "L", "M", "N", "O"]
    parent = ''
    # read data from file as csv entries and parse each line to locate data
    with open(input_file) as csv_file:
        data = csv.reader(csv_file, delimiter=' ')
        for line in data:
            # print('Line:', line, '/n')
            for item in line:
                if(item.find('=') == -1):
                    item.replace(",", "")
                    item.replace(" ", "")
                    if(item[0] in possible_outcomes):
                        parent = item[0]
                if(item.find('=') != -1):
                    # discard remaining comma at the end end of the item
                    # then split key value pair using the delimiter "="
                    item = item.replace(",", "")
                    temp = item.split('=')
                    tree.add_node(temp[0], parent)
                    obtained_inputs[temp[0]] = temp[1][0]
                    print('parent:', parent, ' - child:', item)
                    # print('keys - ', obtained_inputs.keys(), '\n')
    csv_file.close()
    return tree, obtained_inputs


# readFile(Tree(), "tree1.txt")

# ------------------------------------------------------------------------------


def readFileFull(tree, input_file):
    # variable declaration
    obtained_inputs = {}
    possible_outcomes = ["A", "B", "C", "D", "E", "F",
                         "G", "H", "I", "J", "K", "L", "M", "N", "O"]
    parent = ''
    # read data from file as csv entries and parse each line to locate data
    with open(input_file) as csv_file:
        data = csv.reader(csv_file, delimiter=' ')
        for line in data:
            # print('Line:', line, '/n')
            for item in line:
                if(item.find('=') == -1):
                    item.replace(",", "")
                    item.replace(" ", "")
                    if(item[0] in possible_outcomes):
                        parent = item[0]
                if(item.find('=') != -1):
                    # discard remaining comma at the end end of the item
                    # then split key value pair using the delimiter "="
                    item = item.replace(",", "")
                    temp = item.split('=')
                    tree.add_node(temp[0], temp[1], parent)
                    obtained_inputs[temp[0]] = temp[1]
                    print('parent:', parent, ' - child:', item)
                    # print('keys - ', obtained_inputs.keys(), '\n')
    csv_file.close()
    return tree


tree = readFileFull(Tree(), "tree2.txt")
tree.DFS_traversal()
