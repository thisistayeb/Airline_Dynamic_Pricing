from collections import defaultdict
from itertools import product


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.res = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def all_paths(self, u, d, visited, path):

        visited[u] = True
        path.append(u)

        if u == d:
            y = list(path)
            self.res

        else:

            for i in self.graph[u]:
                if visited[i] == False:
                    self.all_paths(i, d, visited, path)

        path.pop()
        visited[u] = False

    def print_all_paths(self, s, d):
        visited = [False] * (self.V)
        path = []
        self.all_paths(s, d, visited, path)
