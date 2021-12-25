from inputs import *
from outputs import *

from equations import *


def main():
    Instructions.displayForMatrixA()

    nodes, branches = map(int, input().split())
    branchName, invBranchName = {}, {}

    graph = Graph(nodes, branches)
    graph.readGraph(branchName, invBranchName)
    treeBranches = graph.findTree(branchName, nodes)

    Instructions.displayForMatrixB()

    values = readCircuitComponents()

    matrixATree = getMatrixATree(treeBranches, invBranchName, nodes, branches)
    matrixALink = getMatrixALink(treeBranches, invBranchName, nodes, branches)

    A = getMatrixA(treeBranches, invBranchName, nodes, branches)
    B = getMatrixB(matrixATree, matrixALink)
    C = getMatrixC(matrixATree, matrixALink)

    print("\nThe Process:\n")

    Formats.formatMatrix(A, "Incidence")
    Formats.formatMatrix(B, "Tie-set")
    Formats.formatMatrix(C, "Cut-set")

    matrixVoltageSource = getMatrixVoltageSource(values[0])
    matrixCurrentSource = getMatrixCurrentSource(values[1])
    matrixImpedence = getMatrixImpedance(values[2])

    iLoop = getMatrixILoop(B, matrixImpedence, matrixCurrentSource, matrixVoltageSource)
    jBranch = getMatrixJBranch(iLoop, B)
    vBranch = getMatrixVBranch(jBranch, matrixImpedence, matrixCurrentSource, matrixVoltageSource);

    Formats.formatMatrix(iLoop, "I Loop");
    Formats.formatMatrix(jBranch, "J Branch");
    Formats.formatMatrix(vBranch, "V Branch");

    branchesOrder = getBranchesOrder(treeBranches, invBranchName)
    Formats.formatResult(jBranch, vBranch, branchesOrder)


if __name__ == "__main__":
    main()
