"""
Algorithms class contains the implementation of DFS and BFS algorithms

Date: 20th July 2020
Authors: Muskan Israni & Keval Varia
Student ID: 017537908, 017834282
Class: CECS 451- Artificial Intelligence
"""

import Graph as Node


class Algorithms:
    # constructor: initializes and assigns the board, the start and end point of the board, lists to keep track of the BFS,DFS paths and fringe.
    def __init__(self, board, startNode, goalNode):
        self.board = board
        self.startNode = startNode
        self.goalNode = goalNode
        self.allNodes = {}
        self.allNodes[self.startNode.get_id()] = self.startNode
        self.allNodes[self.goalNode.get_id()] = self.goalNode
        # keeps track of bfs path
        self.bfsPaths = []
        self.fringe = 0
        # keeps track of dfs path
        self.dfsPaths = []

    # creates neighbors
    def create_neighbor(self, temp, end, lengthof):
        if (end != self.startNode):
            list = []
            for x in range(len(temp)):
                if temp[x] not in self.allNodes:
                    self.allNodes[temp[x]] = Node.Vertex(temp[x])
                    list.append(self.allNodes[temp[x]])
                if temp[x] in self.allNodes:
                    list.append(self.allNodes[temp[x]])
            end.adjacent = list

    # method calls actual BFS method
    def runBFS(self):
        # print("\n\nRunning BFS:\n")
        start = self.startNode
        bfspathtrack = []
        # calls actual BFS with assigned board and start point
        self.bfs(self.board, start)
        temp_node = self.goalNode
        while (temp_node != self.startNode):
            # adding each node to create path
            bfspathtrack.append(temp_node.get_id())
            # moves on to next node
            temp_node = temp_node.parent
        self.bfsPaths = bfspathtrack
        for i in self.allNodes:
            self.allNodes[i].parent = None

    # actual BFS method
    def bfs(self, board, given_node):
        given_node.parent = given_node
        given_node.cost = 0
        queue = []
        # pushes node to queue
        queue.append(given_node)
        while (len(queue) != 0):
            # pops node from queue
            chosen_node = queue.pop(0)
            # increments fringe since node has been visited
            self.fringe = self.fringe + 1
            board.start = chosen_node.get_id()
            # in order to inspect neighbors
            self.create_neighbor(board.calculate_path(), chosen_node, 0)
            # pushing neighbors to list
            for i in chosen_node.adjacent:
                if (i.parent == None):
                    i.parent = chosen_node
                    i.cost = chosen_node.cost + 1
                    queue.append(i)
            if (chosen_node.get_id() == board.get_goal_node()):
                break

    # prints BFS result
    def print_bfs_result(self):
        print("BFS Algorithm output:\nFringe:", self.fringe, "\nCost:", len(self.bfsPaths),
              "\nPath:", self.bfsPaths)
        print(self.Maze(self.bfsPaths))

    # method calls actual DFS method
    def runDFS(self):
        temp = self.startNode
        tempList = self.board.calculate_path()
        list = []
        temp.parent = temp
        for x in range(len(tempList)):
            # adding nodes to list
            list.append(Node.Vertex(tempList[x]))
            self.allNodes[tempList[x]] = list[len(list) - 1]

        for x in range(len(list)):
            # pops from list
            y = list.pop(0)
            # pushes to list
            list.append(y)

            temp.adjacent = list
            time = 0
            # calling the actual DFS method
            self.dfs(self.board, temp, time)

            path = []
            xnode = self.goalNode
            while (xnode != self.startNode):
                path.append(xnode.get_id())
                xnode = xnode.parent
            # adding to get path
            self.dfsPaths.append(path)

            for i in self.allNodes:
                self.allNodes[i].parent = None

    # the actual DFS method
    def dfs(self, board, v, time):
        time = time + 1
        v.start = time
        board.start = v.get_id()

        self.create_neighbor(board.calculate_path(), v, 0)
        for u in v.adjacent:
            # traversing through neighbors
            if (v.get_id() == board.goal + 1):
                pass
            elif (u.parent == None):
                u.parent = v
                self.dfs(board, u, time)
            elif (u.end == None):
                print("Caught in a loop")

    # printing DFS result
    def print_dfs_result(self):
        print("DFS Algorithm output:")
        print("Cost:", len(self.dfsPaths[0]), "\nPath:", self.dfsPaths[0])
        maze_arr = self.Maze(self.dfsPaths[0])
        print(maze_arr, "\n")

    # creating maze using path
    def Maze(self, maze_path):
        data = self.board.data
        width = self.board.size_x
        for x in data:
            if x == "\n":
                data.remove(x)
            if x == "P":
                print()
        for x in maze_path:
            data[x] = "."
        length = len(data) // width
        temp_node = ""
        for i in range(length):
            for j in range(width):
                temp_node = temp_node + data[i * width + j]
            temp_node = temp_node + "\n"
        return temp_node
