from collections import deque
from src.core.graph import Graph

def bfs(graph: Graph, start: str):
    if start not in graph.get_vertices():
        return []

    visited = set([start])
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neigh in graph.get_neighbors(node):
            if neigh not in visited:
                visited.add(neigh)
                queue.append(neigh)

    return result
