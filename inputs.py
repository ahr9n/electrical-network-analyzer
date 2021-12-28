class Graph(object):
    def __init__(self, nodes, branches):
        self.adjacency_list = [[] for _ in range(nodes)]
        self.branch_name = {}
        self.reversed_branch_name = {}
        self.nodes = nodes
        self.branches = branches

    def add_edge(self, edge):
        (from_node, to_node) = edge
        self.adjacency_list[from_node].append(to_node)

    def read_graph(self, branch_name, reversed_branch_name):
        for branch in range(self.branches):
            (from_node, to_node) = tuple(map(int, input().split()))
            self.add_edge((from_node - 1, to_node - 1))
            branch_name[(from_node - 1, to_node - 1)] = self.branch_name[(from_node - 1, to_node - 1)] = branch
            reversed_branch_name[branch] = self.reversed_branch_name[branch] = (from_node - 1, to_node - 1)

    def dfs(self, node, visited, tree_branches, branch_name, same_component, linked=True):
        if visited[node] == 1:
            return
        visited[node] = 1
        same_component[node] = True
        for child in self.adjacency_list[node]:
            if visited[child] != 2:
                if visited[child] != 1:
                    tree_branches.append(branch_name[(node, child)])
                self.dfs(child, visited, tree_branches, branch_name, same_component, linked)
            elif linked and not same_component[node]:
                tree_branches.append(branch_name[(node, child)])
                linked = False
        visited[node] = 2

    def find_tree(self, branch_name, nodes):
        visited = [0] * nodes
        tree_branches = []
        for node in range(nodes):
            if visited[node] == 0:
                self.dfs(node, visited, tree_branches, branch_name, [0] * nodes)
        return tree_branches


def read_circuit_components():
    ret = []
    for i in range(3):
        ret.append(list(map(float, input().split())))
    return ret
