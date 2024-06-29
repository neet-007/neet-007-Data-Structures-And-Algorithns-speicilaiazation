#Uses python3

import sys


def number_of_components(adj):
    visited = [False] * len(adj)
    cc = 0
    def explore(vertex):
        if visited[vertex]:
            return
        visited[vertex] = True
        for edge in adj[vertex]:
            explore(edge)

    for i in range(len(adj)):
        if visited[i]:
            continue

        explore(i)
        cc += 1
    #write your code here
    return cc

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
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
