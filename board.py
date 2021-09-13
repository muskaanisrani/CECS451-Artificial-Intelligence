"""
Constructs a Board data structure made using a 2D array to mimic a matrix

Date: 20th July 2020
Authors: Muskan Israni & Keval Varia
Student ID: 017537908, 017834282
Class: CECS 451- Artificial Intelligence
"""
import numpy as np


class Board(object):
    # default constructor
    def __init__(self, maze_file):
        self.matrix = 0
        self.reset_variables()
        self.data = self.read_data(maze_file)

    # function: reset all variables
    def reset_variables(self):
        self.start = 0
        self.start_x = 0
        self.start_y = 0
        self.goal = 0
        self.goal_x = 0
        self.goal_y = 0
        self.size = 0
        self.size_x = 0

    # function: read data from given file into an array
    def read_data(self, maze_file):
        # variable declaration
        temp_arr = []
        # read file data into matrix
        f = open(maze_file, "r")
        maze_str = f.read()
        # convert input data files into array of strings
        for x in range(len(maze_str)):
            if maze_str[x] != "\n":
                self.size += 1
            temp_arr.append(maze_str[x])
        return temp_arr

    # function: return the start node
    def get_start_node(self):
        return self.start + 1

    # function: locate and return the goal node
    def get_goal_node(self):
        if (self.matrix[self.goal][self.goal+1] == 1):
            return self.goal+1
        if (self.matrix[self.goal][self.goal-1] == 1):
            return self.goal - 1
        if (self.matrix[self.goal][self.goal-self.size_x] == 1):
            return self.goal - self.size_x
        if (self.matrix[self.goal][self.goal + self.size_x] == 1):
            return self.goal + self.size_x
        return self.goal + 1

    # function: print a copy of the maze given the current state of the board.
    def build_matrix(self):
        # variable declaration
        char_arr = []
        str_arr = []
        counter = 0
        temp_matrix = np.zeros((self.size, self.size), dtype=int)

        # variable initialization:
        # char_arr is used to iterate through a line
        # str_arr stores the each line as an array element
        for j in range(len(self.data)):
            if self.data[j] != "\n":
                char_arr.append(self.data[j])
            else:
                self.size_x = len(char_arr)
                str_arr.append(char_arr)
                char_arr = []               # clear char array when end-of-line is reached
        str_arr.append(char_arr)

        # iterate through the matrix and locate the x & y coordinates of the starting node P and goal node "."
        for i in range(len(str_arr)):
            for j in range(len(str_arr[i])):
                if str_arr[i][j] != "%":
                    if str_arr[i][j] == "P":
                        self.start = counter
                        self.start_x = j
                        self.start_y = i
                    if str_arr[i][j] == ".":
                        self.goal = counter
                        self.goal_x = j
                        self.goal_y = i
                    # condition: size validation
                    if i != len(str_arr):
                        # condition: the location below is open
                        if str_arr[i + 1][j] == " " or str_arr[i + 1][j] == ".":
                            temp_matrix[counter][(
                                (i + 1) * len(str_arr[i])) + j] = 1
                    # condition: the location to the immediate left is open
                    if j > 0:
                        if str_arr[i][j - 1] == " " or str_arr[i][j - 1] == ".":
                            temp_matrix[counter][counter - 1] = 1
                    # condition: the location to the immediate right is open
                    if j != len(str_arr[i]):
                        if str_arr[i][j + 1] == " " or str_arr[i][j + 1] == ".":
                            temp_matrix[counter][counter + 1] = 1
                    # condition: the location above is open
                    if i > 0:
                        if str_arr[i - 1][j] == " " or str_arr[i - 1][j] == ".":
                            temp_matrix[counter][(
                                (i - 1) * len(str_arr[i])) + j] = 1
                counter += 1                    # counter update for current location
        self.matrix = temp_matrix
        return temp_matrix

    # function: Return an array of adjacent nodes, given current_node
    def get_adjacent(self, current_node):
        temp_array = []
        # condition: check above node
        if current_node > self.size_x:
            search_node = self.matrix[current_node][current_node - self.size_x]
            if search_node == 1:
                temp_array.append(current_node - self.size_x)
        # condition: check below node
        if current_node + self.size_x < self.size:
            search_node = self.matrix[current_node][current_node + self.size_x]
            if search_node == 1:
                temp_array.append(current_node + self.size_x)
        # condition: check left node
        if current_node % self.size_x > 0:
            search_node = self.matrix[current_node][current_node - 1]
            if search_node == 1:
                temp_array.append(current_node - 1)
        # condition: check right node
        if current_node % self.size_x < self.size_x - 1:
            search_node = self.matrix[current_node][current_node + 1]
            if search_node == 1:
                temp_array.append(current_node + 1)
        return temp_array

    # function:  Return an array of adjacent nodes, given current_node
    def calculate_path(self):
        # variable declaration
        search_node = 0
        temp_array = []
        search_node = 0
        search_complete = False
        # assign starting node
        temp_array.append(self.start)
        # iterate through each node in the array to calculate path
        while not search_complete:
            current_node = temp_array.pop()
            # condition: check above nodeF
            if current_node > self.size_x:
                search_node = self.matrix[current_node][current_node - self.size_x]
                if search_node == 1:
                    temp_array.append(current_node - self.size_x)
                    search_complete = True
            # condition: check left node
            if current_node % self.size_x > 0:
                search_node = self.matrix[current_node][current_node - 1]
                if search_node == 1:
                    temp_array.append(current_node - 1)
                    search_complete = True
            # condition: check right node
            if current_node % self.size_x < self.size_x - 1:
                search_node = self.matrix[current_node][current_node + 1]
                if search_node == 1:
                    temp_array.append(current_node + 1)
                    search_complete = True
            # condition: check below node
            if current_node + self.size_x < self.size:
                search_node = self.matrix[current_node][current_node + self.size_x]
                if search_node == 1:
                    temp_array.append(current_node + self.size_x)
                    search_complete = True
            return temp_array
