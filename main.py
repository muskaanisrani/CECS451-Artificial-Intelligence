"""
Runner Program to simulate pruning of a minmax tree

Date: August 4th, 2021
Authors: Keval Varia, Muskan Israni
Student ID: 017834282, 017537908
Class: CECS 451- Artificial Intelligence
"""

from Tree import *


def main():
    # variable declaration
    small_tree = Tree()
    big_tree = Tree()
    inputFile1 = "tree1.txt"
    inputFile2 = "tree2.txt"

    # read input file into a tree
    print("\nPart I: Import data from CSV file to Tree structure\n")
    small_tree.populateTree(inputFile1)
    big_tree.populateTree(inputFile2)

    # part 2 - perform a minimax algorithm (w/o alpha-beta) on both trees generated above
    small_tree.minimaxSimple(small_tree.root, small_tree.get_depth())
    big_tree.minimaxSimple(big_tree.root, big_tree.get_depth())

    # display the results of the minmax algorithm run in the step above for both trees
    print("Part II - Small File: Minimax:")
    small_tree.DFS_traversal()
    print("\nPart II - Big File: Minimax:")
    big_tree.DFS_traversal()

    # part 3 - perform a minimax algorithm (w alpha-beta pruning) on both trees generated above
    print("\n\nPart III - Small File - Minimax w/ Alpha-Beta:")
    small_tree.minimaxComplex(small_tree.root, small_tree.get_depth())
    print("\nPart III - Big File - Minimax w/ Alpha-Beta:")
    big_tree.minimaxComplex(big_tree.root, big_tree.get_depth())

    # display the results of the minmax algorithm run in the step above for both trees
    for item in small_tree.get_nodes():
        node = small_tree.nodes[item]
        print(node.get_id(), "[", node.get_weight(), "]", node.get_pruned())
    for item in big_tree.get_nodes():
        node = big_tree.nodes[item]
        print(node.get_id(), "[", node.get_weight(), "]", node.get_pruned())


# auto-run main method at program launch/run
if __name__ == '__main__':
    main()
