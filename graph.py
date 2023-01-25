class Node:
    def __init__(self, data):
        self.data = data
        self.edges = []

    def add_edge(self, data):
        if len(self.edges) < 1:
            self.edges.append(Node(data))

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

    def find_common_neighbors(self, node_0, node_1):
        return_nodes = {}
        for node in self.nodes:
            return_nodes[node] = []
            if node.data == node_0 or node.data == node_1:
                return_nodes[node].append(set(self.nodes_reachable_from(node)))
        common_neighbors = set([])
        for k in return_nodes:
            for edges in return_nodes[k]:
                if len(common_neighbors) == 0:
                    common_neighbors = set(edges)
                else:
                    common_neighbors = common_neighbors & set(edges)
        if len(common_neighbors) > 1:
            return max(common_neighbors)
        else:
            return list(common_neighbors)[0]

    def nodes_reachable_from(self, node):
        # For each nodes' edges, search all available nodes
        queue = [node]
        visited = []
        return self.search_nodes(visited, queue)

    def search_nodes(self, visited, queue):
        while queue:
            for node in queue:
                queue.pop(0)
                visited.append(node.data)
                for edge in node.edges:
                    queue.append(edge)
        return set(visited)

    def bfs(self):
        visited = []
        queue = self.nodes
        self.search_nodes(visited, queue)

nodes = []
node = Node(1)
node.add_edge(2)
nodes.append(node)
node = Node(0)
node.add_edge(2)
nodes.append(node)
graph = Graph(nodes)
print(graph.find_common_neighbors(0,1)==2)

nodes = []
node = Node(0)
node.add_edge(1)
node.edges[0].add_edge(2)
nodes.append(node)
graph = Graph(nodes)
print(graph.find_common_neighbors(0,2)==2)




