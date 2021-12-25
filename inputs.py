class Graph(object):
    def __init__(self, nodes, branches):
        self.adjList = [[] for i in range(nodes)]
        self.branchName = {}
        self.invBranchName = {}
        self.nodes = nodes
        self.branches = branches

    def addEdge(self, edge):
        fromNode, toNode = (edge)
        self.adjList[fromNode].append(toNode)

    def readGraph(self, branchName, invBranchName):
        for branch in range(self.branches):
            (fromNode, toNode) = tuple(map(int, input().split()))
            self.addEdge((fromNode - 1, toNode - 1))
            branchName[(fromNode - 1, toNode - 1)] = self.branchName[(fromNode - 1, toNode - 1)] = branch
            invBranchName[branch] = self.invBranchName[branch] = (fromNode - 1, toNode - 1)

    def dfs(self, node, visited, treeBranches, branchName, sameComponent, linked = True):
        if visited[node] == 1:
            return
        visited[node] = 1
        sameComponent[node] = True
        for child in self.adjList[node]:
            if visited[child] != 2:
                if visited[child] != 1:
                    treeBranches.append(branchName[(node, child)])
                self.dfs(child, visited, treeBranches, branchName, sameComponent, linked)
            elif(linked and sameComponent[node] == False):
                treeBranches.append(branchName[(node, child)])
                linked = False
        visited[node] = 2

    def findTree(self, branchName, nodes):
        visited = [0] * nodes
        treeBranches = []
        for node in range(nodes):
            if visited[node] == 0:
                self.dfs(node, visited, treeBranches, branchName, [0] * nodes)
        return treeBranches

def readCircuitComponents(branches):
    ret = []
    for i in range(3):
        ret.append(list(map(float, input().split())))
    print(ret)
    return ret