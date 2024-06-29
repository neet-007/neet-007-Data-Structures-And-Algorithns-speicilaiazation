#Uses python3

import sys

sys.setrecursionlimit(200000)


def number_of_strongly_connected_components(adj):
    n = len(adj)
    adj_r = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            adj_r[v].append(u)

    order = []
    visited = [False] * n

    def dfs1(v):
        visited[v] = True
        for neighbor in adj[v]:
            if not visited[neighbor]:
                dfs1(neighbor)
        order.append(v)

    def dfs2(v):
        visited[v] = True
        for neighbor in adj_r[v]:
            if not visited[neighbor]:
                dfs2(neighbor)

    for i in range(n):
        if not visited[i]:
            dfs1(i)

    visited = [False] * n
    scc_count = 0

    while order:
        v = order.pop()
        if not visited[v]:
            dfs2(v)
            scc_count += 1

    return scc_count

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
    print(number_of_strongly_connected_components(adj))
