#Uses python3

import sys


def acyclic(adj:list[list[int]]):
    visited = [False] * len(adj)

    def explore(vertex:int, origin:int, first:bool=False):
        if vertex == origin and not first:
            return 1
        if visited[vertex]:
            return 0
        visited[vertex] = True

        res = 0
        for edge in adj[vertex]:
            res = explore(edge, origin)
            if res:
                break

        return res
    res_ = 0
    for vertex in range(len(adj)):
        visited[vertex] = False
        res_ = explore(vertex, vertex, True)
        if res_:
            break

    return res_

if __name__ == '__main__':
    #sys.stdin = open('input.txt', 'r')
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
