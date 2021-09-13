"""
Constructs a Graph data structure

Date: 12th July 2020
Authors: Muskan Israni & Keval Israni
Student ID: 017537908, 017834282
class: CECS 451- Artificial Intelligence
"""

class Graph(object):
    # constructor for class Graph
    def __init__(self):
        #creates a new dictionary and initializes it
        self.vert_dict= {}
        self.num_vertices=0

    # add a new vertex to the graph
    def add_vertex(self,node):
        #creating a new vertex object
        new_v= Vertex(node)
        #adding a vertex in a dictionary where key is a node label
        #and the value is the vertex object
        self.vert_dict[node]= new_v
        #incrementing dictionary count by 1
        self.num_vertices= self.num_vertices + 1

    # retrieve a vertex from the graph
    def get_vertex(self,node):
        return self.vert_dict[node].key()

    #add an edge between two existing vertices
    def add_edge(self, from_edge, to_edge, weight):
        if from_edge not in self.vert_dict:
            self.add_vertex(from_edge)
        if to_edge not in self.vert_dict:
            self.add_vertex(to_edge)
        self.vert_dict[from_edge].add_neighbor(self.vert_dict[to_edge],weight)

    #get all vertices currently available in the graph
    def get_vertices(self):
        return self.vert_dict.keys()

    #print each link between vertices in the form of "start vertex, end vertex, weight"
    def graph_summary(self):
        # print ("\nPrinting graph summary")
        #obtain start node, obtain all linked end nodes, print the directional connection to console
        for node in self.get_vertices():
            for key in self.vert_dict[node].get_connections():
                print(node, key.get_id(), self.vert_dict[node].get_weight(key))
        # print ("Completed printing graph summary\n")


# Vertex supporting class to be used in Graph
class Vertex:
    # constructor for class Vertex
    def __init__(self, node):
        self.id=node
        #a dictionary to keep track of the neighbors
        self.adjacent={}

    # retrieve all connections for current node/vertex
    def get_connections(self):
        return self.adjacent

    # add a new neighbor to the current node/vertex
    def add_neighbor(self, obj_neighbor, weight):
        self.adjacent[obj_neighbor]= weight
        # print("weight:", self.adjacent[obj_neighbor])

    # retrieve ID value for current node/vertex
    def get_id(self):
        return self.id

    # retrieve weight between current node and target node
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]


# main method as a runner code
def main():
    # variable delcaration
    g= Graph()
    print ("Graph created.\n")

    #variable initialization
    g.add_vertex('S')
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_vertex('D')
    print ("Vertices initialized\n")

    # link all vertices
    g.add_edge('S', 'A', 10)
    g.add_edge('S', 'C', 5)
    g.add_edge('A', 'C', 2)
    g.add_edge('A', 'B', 1)
    g.add_edge('B', 'D', 4)
    g.add_edge('C', 'A', 3)
    g.add_edge('C', 'B', 9)
    g.add_edge('C', 'D', 2)
    g.add_edge('D', 'B', 6)
    g.add_edge('D', 'S', 7)
    print ("Edges linked to vertices\n")

    # print all connections in the graph
    print ("Printing Graph Summary\n") 
    g.graph_summary()
    print ("\nThank you for using our program!\n")

# auto-run main method at program launch/run
if __name__ == '__main__':
    main()