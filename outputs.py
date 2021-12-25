import numpy as np


class Instructions(object):
    @staticmethod
    def displayForMatrixA():
        print("         Welcome to the Electrical Network Analyzer!\n\n"
              "Input WiKi for matrix A:\n"
              "     The first line contains two integers; N, M:\n"
              "     - N is the number of nodes, and M is the number of branches in the directed graph of the network, respectively.\n"
              "     - The next M lines contain the edges of the graph, each in the form of two integers: U, V (1 <= U, V <= N);\n"
              "     (In other words: U and V are the end-points of the nodes that are connected by the branch).\n"
              "Important Note:\n"
              "     - The input order of the branches ARE SORTED from \'a\' (till the end using ASCII code).\n\n"
              "The input:\n")

    @staticmethod
    def displayForMatrixB():
        print("\nInput WiKi for matrix B:\n"
              "     The next three lines represent the voltage sources, the current sources and the resistances on the branches:\n"
              "     Each line contains four values; b d a c (all respectively).\n")


class Formats(object):
    @staticmethod
    def formatMatrix(matrix, matrixType):
        x = np.random.random(10)
        with np.printoptions(precision=5, suppress=True):
            print("Matrix:", matrixType, '\n', np.array(matrix), '\n')

    @staticmethod
    def formatResult(matrixJBranch, matrixVBranch, branchesOrder):
        print("The result:\n",
              "                    Voltage (V)     Current (A)\n",
              "     ---------      -----------     -----------")
        for i in range(len(branchesOrder)):
            print("      Branch ", branchesOrder[i] + 1, ":      ", end='', sep='')
            if matrixVBranch[0][i] > 0:
                print(" ", end='')
            print(round(matrixVBranch[0][i], 7), "      ", end='', sep='')
            if matrixJBranch[0][i] > 0:
                print(" ", end='')
            print(round(matrixJBranch[0][i], 7))
        print("      ---------      -----------     -----------")
