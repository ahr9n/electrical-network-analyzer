from inputs import *
from outputs import *

from equations import *

def main():
    Instructions.displayForMatrixA()

    nodes, branches = 0, 0
    branchName, invBranchName = {}, {}

    graph = Graph.readGraph(branchName, invBranchName, nodes, branches)
    treeBranches = Graph.findTree(graph, branchName, nodes, branches)

    Instructions.displayForMatrixB()

    matrixATree = getMatrixATree(treeBranches, invBranchName, nodes, branches)
    matrixALink = getMatrixALink(treeBranches, invBranchName, nodes, branches)

    A = getMatrixA(treeBranches, invBranchName, nodes, branches)
    B = getMatrixB(matrixATree, matrixALink)
    C = getMatrixC(matrixATree, matrixALink)

    Formats.formatMatrix(A, "Incidence")
    Formats.formatMatrix(B, "Tie-set")
    Formats.formatMatrix(C, "Cut-set")

    values = readCircuitComponents(branches)
    matrixVoltageSource = getMatrixVoltageSource(values[0])
    matrixCurrentSource	= getMatrixCurrentSource(values[1])
    matrixImpedence = getMatrixImpedance(values[2])

    iLoop = getMatrixILoop(B, matrixImpedence, matrixCurrentSource, matrixVoltageSource)

    jBranch = getMatrixJBranch(iLoop, B)
    vBranch = getMatrixVBranch(jBranch, matrixImpedence, matrixCurrentSource, matrixVoltageSource);

    Formats.formatMatrix(iLoop, "I Loop");
    Formats.formatMatrix(jBranch, "J Branch");
    Formats.formatMatrix(vBranch, "V Branch");

    branchesOrder = getBranchesOrder(treeBranches, invBranchName)
    Formats.formatResult(vBranch, jBranch, branchesOrder)

if __name__ == "__main__":
    main()