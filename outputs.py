from equations import *
import numpy as np


class Instructions:
    @staticmethod
    def display_for_matrix_a():
        print("         Welcome to the Electrical Network Analyzer!\n\n"
              "Input WiKi for matrix A:\n"
              "     The first line contains two integers; N, M:\n"
              "     - N is the number of nodes, and M is the number of branches "
              "in the directed graph of the network, respectively.\n"
              "     - The next M lines contain the edges of the graph, "
              "each in the form of two integers: U, V (1 <= U, V <= N);\n"
              "     (In other words: U and V are the end-points of the nodes that are connected by the branch).\n"
              "\nImportant Note:\n"
              "     - The input order of the branches ARE SORTED from \'1\' till the end.\n\n"
              "The input:\n")

    @staticmethod
    def display_for_matrix_b(tree_branches, reversed_branch_name):
        branches_order = get_branches_order(tree_branches, reversed_branch_name)
        branches_order = [branches_order[i] + 1 for i in range(len(branches_order))]
        print("\nInput WiKi for matrix B:\n"
              "     The next three lines represent the voltage sources, "
              "the current sources and the resistances on the branches:\n"
              f"     Each line contains {len(branches_order)} values; {branches_order} (all respectively).\n")
        print("The branches are in the following order:\n",
              "     Voltage sources: ", branches_order, '\n',
              "     Current sources: ", branches_order, '\n',
              "     Resistors:       ", branches_order, '\n', sep='')


class Formats:
    @staticmethod
    def format_matrix(matrix, matrix_type):
        with np.printoptions(precision=5, suppress=True):
            print("Matrix:", matrix_type, '\n', np.array(matrix), '\n')

    @staticmethod
    def format_result(matrix_j_branch, matrix_v_branch, branches_order):
        print("The result:\n",
              "                    Voltage (V)     Current (A)\n",
              "     ---------      -----------     -----------")
        for i in range(len(branches_order)):
            print("      Branch ", branches_order[i] + 1, ":      ", end='', sep='')
            if matrix_v_branch[0][i] > 0:
                print(" ", end='')
            print(round(matrix_v_branch[0][i], 7), "      ", end='', sep='')
            if matrix_j_branch[0][i] > 0:
                print(" ", end='')
            print(round(matrix_j_branch[0][i], 7))
        print("      ---------      -----------     -----------")
