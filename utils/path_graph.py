from collections import defaultdict


def find_all_parents(G, s):
    Q = [s]
    parents = defaultdict(set)
    while len(Q) != 0:
        v = Q[0]
        Q.pop(0)
        for w in G.get(v, []):
            parents[w].add(v)
            Q.append(w)
    return parents


def find_all_paths(parents, a, b):
    return [y + b for x in list(parents[b]) for y in find_all_paths(parents, a, x)]
