"""
Constructs a Graph data structure.
- Modified from Lab 2 to be used in Project 2
 -- added parent attribute to vertex class
 -- added end attribute to vertex class

Date: 20th July 2020
Authors: Muskan Israni & Keval Varia
Student ID: 017537908, 017834282
Class: CECS 451- Artificial Intelligence
"""


class Graph(object):
    # constructor for class Graph
    def __init__(self):
        # creates a new dictionary and initializes it
        self.vert_dict = {}
        self.num_vertices = 0

    # add a new vertex to the graph

    def add_vertex(self, node):
        # creating a new vertex object
        new_v = Vertex(node)
        # adding a vertex in a dictionary where key is a node label
        # and the value is the vertex object
        self.vert_dict[node] = new_v
        # incrementing dictionary count by 1
        self.num_vertices = self.num_vertices + 1

    # retrieve a vertex from the graph
    def get_vertex(self, node):
        return self.vert_dict[node].key()

    # add an edge between two existing vertices
    def add_edge(self, from_edge, to_edge, weight):
        if from_edge not in self.vert_dict:
            self.add_vertex(from_edge)
        if to_edge not in self.vert_dict:
            self.add_vertex(to_edge)
        self.vert_dict[from_edge].add_neighbor(self.vert_dict[to_edge], weight)

    # get all vertices currently available in the graph
    def get_vertices(self):
        return self.vert_dict.keys()

    # print each link between vertices in the form of "start vertex, end vertex, weight"
    def graph_summary(self):
        # print ("\nPrinting graph summary")
        # obtain start node, obtain all linked end nodes, print the directional connection to console
        for node in self.get_vertices():
            for key in self.vert_dict[node].get_connections():
                print(node, key.get_id(), self.vert_dict[node].get_weight(key))
        # print ("Completed printing graph summary\n")


# Vertex supporting class to be used in Graph
class Vertex:
    # constructor for class Vertex
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.parent = None
        self.end = 0

    # assign a parent to the current node
    def set_parent(self, parent):
        self.parent = parent

    # retrieve a parent for the current node
    def get_parent(self):
        return self.parent

    # retrieve all connections for current node/vertex
    def get_connections(self):
        return self.adjacent

    # add a new neighbor to the current node/vertex
    def add_neighbor(self, obj_neighbor, weight):
        self.adjacent[obj_neighbor] = weight
        # print("weight:", self.adjacent[obj_neighbor])

    # retrieve ID value for current node/vertex
    def get_id(self):
        return self.id

    # retrieve weight between current node and target node
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]


#
# def main():
#
#     print("Graph 1 -----------------")
#     graph1 = Graph()
#     a = Vertex("a")
#     b = Vertex("b")
#     c = Vertex("c")
#     d = Vertex("d")
#     s = Vertex("s")
#
#     nodes = [a,b,c,d,s]
#     for x in range (len(nodes)):
#         graph1.add_vertex(nodes[x])
#
#     edge = [(a,c,2),(c,a,3),(a,b,1),(c,d,2),(c,b,9),
#             (s,c,5),(s,a,10),(d,s,7),(d,b,6),
#             (b,d,4)]
#
#     for y in range(len(edge)):
#         graph1.add_edge(edge[y][0], edge[y][1], edge[y][2])
#
#
#     graph1.graph_summary()
#     # print(a.get_adjID())
#     # print(graph1.get_vertex(a))
#     # print(graph1.get_vertices())
#
# main()
