import numpy as np

def getBranchesOrder(treeBranches, invBranchName):
    branchesOrder = treeBranches.copy()
    treeBranches.sort()
    for key, value in invBranchName.items():
        if key not in treeBranches:
            branchesOrder.append(key)
    return branchesOrder

def getMatrixA(treeBranches, invBranchName, nodes, branches):
    branchesOrder = getBranchesOrder(treeBranches, invBranchName)
    A = [[0 for j in range(branches)] for i in range(nodes)]
    for branch in range(branches):
        (key, value) = invBranchName[branchesOrder[branch]]
        A[key][branch], A[value][branch] = 1, -1
    return A

def getMatrixATree(treeBranches, invBranchName, nodes, branches):
    A = getMatrixA(treeBranches, invBranchName, nodes, branches)
    matrixATree = []
    for i in range(nodes - 1):
        matrixATree.append([])
        for j in range(len(treeBranches)):
            matrixATree[i].append(A[i][j])
    return matrixATree

def getMatrixALink(treeBranches, invBranchName, nodes, branches):
    A = getMatrixA(treeBranches, invBranchName, nodes, branches)
    matrixALink = []
    for i in range(nodes - 1):
        matrixALink.append([])
        for j in range(len(treeBranches), branches):
            matrixALink[i].append(A[i][j])
    return matrixALink

def getMatrixCLink(matrixATree, matrixALink):
    aTree = np.array(matrixATree)
    aTreeInverse = np.linalg.inv(aTree)
    # aTreeInverse = aTree ^ -1
    matrixCLink = np.dot(aTreeInverse, matrixALink)
    return matrixCLink

def getMatrixBTree(matrixATree, matrixALink):
    matrixCLink = getMatrixCLink(matrixATree, matrixALink)
    matrixBTree = np.multiply(np.transpose(matrixCLink), -1)
    matrixBTree[matrixBTree == -0] = 0  # avoiding '-0'
    return matrixBTree

def getMatrixC(matrixATree, matrixALink):
    matrixCLink = getMatrixCLink(matrixATree, matrixALink)
    matrixCTree = np.identity(len(matrixCLink))
    matrixC = np.concatenate((matrixCTree, matrixCLink), axis=1)
    return matrixC

def getMatrixB(matrixATree, matrixALink):
    matrixBTree = getMatrixBTree(matrixATree, matrixALink)
    matrixBLink = np.identity(len(matrixBTree))
    matrixB = np.concatenate((matrixBTree, matrixBLink), axis=1)
    return matrixB

def getMatrixImpedance(resistors):
    matrixImpedance = []
    for i in range(len(resistors)):
        helper = [0 for i in range(len(resistors))]
        helper[i] = resistors[i]
        matrixImpedance.append(helper)
    # matrixImpedance = np.dot(matrixImpedance, np.identity(len(resistors)))
    return matrixImpedance

def getMatrixCurrentSource(currentSources):
    matrixCurrentSource = [[currentSources[i]] for i in range(len(currentSources))]
    return matrixCurrentSource

def getMatrixVoltageSource(voltageSources):
    matrixVoltageSource = [[voltageSources[i]] for i in range(len(voltageSources))]
    return matrixVoltageSource

def getMatrixILoop(matrixB, matrixImpedance, matrixCurrentSource, matrixVoltageSource):
    rightSide = np.subtract(np.dot(matrixB, matrixVoltageSource), np.dot(matrixB, np.dot(matrixImpedance, matrixCurrentSource)))
    leftSide = np.dot(matrixB, np.dot(matrixImpedance, np.transpose(matrixB)))
    leftSideInverse = np.linalg.inv(leftSide)
    matrixILoop = np.dot(leftSideInverse, rightSide)
    return matrixILoop

def getMatrixJBranch(matrixB, matrixILoop):
    matrixJBranch = np.dot(np.transpose(matrixB), matrixILoop)
    return matrixJBranch

def getMatrixVBranch(matrixJBranch, matrixImpedance, matrixCurrentSource, matrixVoltageSource):
    helper = np.subtract(np.dot(matrixImpedance, np.add(matrixJBranch, matrixCurrentSource)), matrixVoltageSource)
    matrixVBranch = [helper[i][i] for i in range(len(helper))]
    return matrixVBranch
