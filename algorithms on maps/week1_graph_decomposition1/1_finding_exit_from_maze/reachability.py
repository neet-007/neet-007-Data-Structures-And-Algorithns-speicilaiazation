#Uses python3

import sys

def reach(adj, x, y):
    #write your code here
    visited = [[False, -1, -1] for _ in range(len(adj))]
    clock = 0
    def recurse(vertex:int):
        nonlocal clock
        if visited[vertex][0]:
            return
        clock += 1
        visited[vertex][1] = clock
        visited[vertex][0] = True
        for neighbour in adj[vertex]:
            recurse(neighbour)
        clock += 1
        visited[vertex][2] = clock

    recurse(0)
    if (visited[x][1] < visited[y][1] and visited[y][2] < visited[x][2]) or (visited[y][1] < visited[x][1] and visited[x][2] < visited[y][2]):
        return 1
    return 0

if __name__ == '__main__':
    #sys.stdin = open('input.txt', 'r')
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
