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
        print("Input WiKi for matrix B:\n"
              "     The next three lines represent the voltage sources, the current sources and the resistances on the branches:\n"
              "     Each line contains four values; b d a c (all respectively).\n")

class Formats(object):
    @staticmethod
    def formatMatrix(matrix, matrixType):
        print("     Matrix:", matrixType)
        print(matrix)

    @staticmethod
    def formatResult(matrixJBranch, matrixVBranch, branchesOrder):
        print("The result:\n",
              "                           Voltage (V)         Current (A)\n",
              "     ---------------     ---------------     ---------------")
        for i in range(len(branchesOrder)):
            print("     Branch", branchesOrder[i], ":     ", matrixVBranch[i][0], "     ", matrixJBranch[i][0])
        print("     ---------------     ---------------     ---------------")