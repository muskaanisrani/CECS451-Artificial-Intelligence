"""
Constructs a Tree data structure

Date: August 4th, 2021
Authors: Keval Varia, Muskaan Israni
Student ID: 017834282, 017537908
class: CECS 451- Artificial Intelligence
"""

import csv


class Tree(object):
    def __init__(self):
        self.nodes = {}
        self.node_count = 0
        self.root = None
        self.depth = 0

    def add_node(self, node_id, node_weight, parent_id):
        # # if the node doesn't already exist
        # if node_id not in self.nodes:
        # add as root node or as a child to an existing node
        if len(parent_id) == 0:
            parent = None
            new_node = Node(node_id, node_weight, parent)
            self.root = new_node
        else:
            parent = self.nodes[parent_id]
            new_node = Node(node_id, node_weight, parent)
            parent.add_child(node_id, new_node)
        # update tree entries list and node count
        self.nodes[node_id] = new_node
        self.node_count += 1

    # Obtain the node given a node ID ~ as long as it exists
    def get_node(self, node_id):
        if node_id in self.nodes:
            return self.nodes[node_id]
        else:
            return None

    # Obtain all nodes currently present in the tree
    def get_nodes(self):
        return self.nodes

    # Perform DFS on the current state of the tree
    def DFS_util(self, node):
        for item in node.get_children_node():
            if item.visited == False:
                self.DFS_util(item)
                item.visited = True
        print(node.get_id(), '[', int(node.get_weight()), ']')

    # DFS trigger runner
    def DFS_traversal(self):
        self.DFS_util(self.root)

    # DFS inspired metodology to determine the depth of the tree in its current state
    def count_util(self, node):
        if node is None:
            return 0
        for item in node.get_children_node():
            temp = self.nodes[item.get_id()]
            self.depth += 1
            self.count_util(temp)
            return self.depth

    # DFS depth finder trigger runner
    def get_depth(self):
        return self.count_util(self.root)

    # Import data from CSV file into tree nodes
    def populateTree(self, input_file):
        # local variable declaration
        possible_outcomes = ["A", "B", "C", "D", "E", "F",
                             "G", "H", "I", "J", "K", "L", "M", "N", "O"]
        parent = ''
        # read data from file as csv entries and parse each line to locate data
        with open(input_file) as csv_file:
            data = csv.reader(csv_file, delimiter=' ')
            for line in data:
                for item in line:
                    if(item.find('=') == -1):
                        item.replace(",", "")
                        if(item[0] in possible_outcomes):
                            parent = item[0]
                    if(item.find('=') != -1):
                        # discard remaining comma at the end end of the item
                        # then split key value pair using the delimiter "="
                        item = item.replace(",", "")
                        temp = item.split('=')
                        self.add_node(temp[0], temp[1], parent)
        # close file after use for parallel programs to access
        csv_file.close()

    # Minmax without alpha-beta values
    def minimaxSimple(self, node, depth):
        self.max_value(node, depth)

    # Minmax with alpha-beta values
    def minimaxComplex(self, node, depth):
        self.max_value_prune(node, float('-inf'), float('inf'), depth)

    # obtain max without alpha-beta values ~ as per textbook
    def max_value(self, node, depth):
        if depth == 0:
            return node.get_weight()
        temp_max = float('-inf')
        for child in node.get_children_node():
            e = self.min_value(child, depth - 1)
            temp_max = max(temp_max, e)
            node.weight = temp_max
        return temp_max

    # obtain min without alpha-beta values ~ as per textbook
    def min_value(self, node, depth):
        if depth == 0:
            return node.get_weight()
        temp_min = float('inf')
        # visit each child of the current node to find the minimum between their values
        for child in node.get_children_node():
            e = self.max_value(child, depth - 1)
            temp_min = min(temp_min, e)
            node.weight = temp_min
        return temp_min

    # print the resulting node values after running pruning with minimax
    def gather_result(self, node):
        if(node is self.root):
            print(node.get_id(),
                  '[', node.get_weight(), ']', node.get_pruned())
        for child in node.get_children_node():
            print(child.get_id(),
                  '[', child.get_weight(), ']', child.get_pruned())

    # DFS inspired print function trigger
    def print_result(self):
        self.gather_result(self.root)

    # obtain max using alpha-beta values ~ as per textbook
    def max_value_prune(self, node, a, b, depth):
        # reached base case
        if depth == 0:
            return node.get_weight()
        # continue
        for child in node.get_children_node():
            child.pruned = True
            a = max(a, self.min_value_prune(child, a, b, depth - 1))
            if(a != float('-inf')):
                node.weight = a
            if b <= a:
                return a
        return a

    # obtain min using alpha-beta values ~ as per textbook
    def min_value_prune(self, node, a, b, depth):
        if depth == 0:
            return node.get_weight()
        for child in node.get_children_node():
            child.pruned = True
            b = min(b, self.max_value_prune(child, a, b, depth - 1))
            if(b != float('inf')):
                node.weight = b
            if b <= a:
                return b
        return b


class Node():
    # class constructor
    def __init__(self, id, weight, parent):
        self.id = id
        self.weight = float(weight)
        self.parent = parent
        self.pruned = False
        self.visited = False
        self.children = []

    # add a child to the current node
    def add_child(self, child_id, child_node):
        if child_id not in self.children:
            self.children.append(child_node)

    # retrieve the list of children for current node
    def get_children_node(self):
        return self.children

    # retrieve the parent to the current node
    def get_parent(self):
        return self.parent

    # retrieve the ID for the current node
    def get_id(self):
        return self.id

    # retrieve the weight
    def get_weight(self):
        return self.weight

    # retrieve a boolean value demonstrating whether the current node is pruned
    def get_pruned(self):
        return self.pruned


# ------------- unused functions developed using psuedocode from https://www.youtube.com/watch?v=l-hh51ncgDI ----------------

"""
    def minimax(self, position, depth, a, b, maximPlayer):
        maxValue = 0
        minValue = 0
        if depth == 0:
            return position.get_weight()
        if maximPlayer:
            # maxValue=float('-inf')
            for children in position.get_children_node():
                e = self.minimaxx(children, depth - 1, a, b, False)
                maxValue = max(maxValue, e)
                a = max(a, e)
                if b <= a:
                    break
            return maxValue
        else:
            # minValue =float('inf')
            for children in position.get_children_node():
                e = self.minimaxx(children, depth - 1, a, b, True)
                minValue = min(minValue, e)
                b = min(b, e)
                if b <= a:
                    break
            return minValue



    # minimax without the alpha-beta pruning
    def minimax(self, position, depth, maximizingPlayer):
        if(depth == 0):
            return (position)
        if(maximizingPlayer):
            maxEval = (-1000)
            for child in position.get_children_node():
                eval = self.minimax(child, depth - 1, False)
                maxEval = max(maxEval, eval)
            return maxEval
        else:
            minEval = 1000
            for child in position.get_children_node():
                eval = self.minimax(child, depth - 1, True)
                minEval = min(minEval, eval)
            return minEval

"""
