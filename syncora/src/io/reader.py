import json
from src.core.graph import Graph

def load_graph(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    graph = Graph(directed=data.get('directed', False))

    for v in data['vertices']:
        graph.add_vertex(v)

    for u, v in data['edges']:
        graph.add_edge(u, v)

    return graph
