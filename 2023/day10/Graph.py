from collections import defaultdict


class Graph:
    def __init__(self):
        self.edges = defaultdict(set)
        self.vertices = []

    def add_edge(self, vertex_1, vertex_2):
        self.edges[vertex_1].add(vertex_2)

    def add_vertex(self, new_vertex):
        self.vertices.append(new_vertex)
