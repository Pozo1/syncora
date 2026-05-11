class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self._adj = {}

    def add_vertex(self, v):
        if v not in self._adj:
            self._adj[v] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self._adj[u].append(v)
        if not self.directed:
            self._adj[v].append(u)

    def get_neighbors(self, v):
        return self._adj.get(v, [])

    def get_vertices(self):
        return list(self._adj.keys())
