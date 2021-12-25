class Graph(object):
    def __init__(self):
        self.adjList = {}
        self.branchName = {}
        self.invBranchName = {}
        self.nodes = 0
        self.branches = 0

    def addEdge(self, edge):
        fromNode, toNode = (edge)
        if fromNode not in self.adjList:
            self.adjList[fromNode] = []
        self.adjList[fromNode].append(toNode)

    def readGraph(self, branchName, invBranchName, nodes, branches):
        n, m = map(int, input().split())
        nodes += n
        branches += m
        for branch in range(branches):
            edge = tuple(map(int, input().split()))
            self.addEdge(edge)
            branchName[edge] = branch
            invBranchName[branch] = edge

    def dfs(self, node, visited, treeBranches, branchName, sameComponent, linked = True):
        if visited[node] == 1:
            return
        visited[node] = 1
        sameComponent.add(node)

        for child in self.adjList[node]:
            if visited[child] != 2:
                if visited[child] != 1:
                    treeBranches.append(branchName[{node, child}])
                    self.dfs(child, visited, treeBranches, branchName, sameComponent, linked)
            elif(linked and node not in sameComponent):
                treeBranches.append(branchName[{node, child}])
                linked = False
        visited[node] = 2

    def findTree(self, graph, branchName, nodes, branches):
        visited = [0] * nodes
        treeBranches = []
        sameComponent = set()
        for node in range(nodes):
            if visited[node] == 0:
                sameComponent = set()
                self.dfs(node, visited, treeBranches, branchName, sameComponent)
        return treeBranches


def readCircuitComponents(branches):
    ret = {}
    for i in range(3):
        ret[i] = []
        for branch in range(branches):
            now = eval(input())
            ret[i].append(now)
    return ret