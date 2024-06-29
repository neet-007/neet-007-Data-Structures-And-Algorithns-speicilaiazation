#Uses python3

import sys
import queue


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    n = len(adj)
    distance[s] = 0
    reachable[s] = 1
    
    # Bellman-Ford algorithm to find shortest paths
    for i in range(n - 1):
        for u in range(n):
            if distance[u] == float('inf'):
                continue
            for idx, v in enumerate(adj[u]):
                if distance[v] > distance[u] + cost[u][idx]:
                    distance[v] = distance[u] + cost[u][idx]
                    reachable[v] = 1

    # Check for negative cycles
    for i in range(n):
        for u in range(n):
            if distance[u] == float('inf'):
                continue
            for idx, v in enumerate(adj[u]):
                if distance[v] > distance[u] + cost[u][idx]:
                    # If we can still relax an edge, then there is a negative cycle
                    distance[v] = distance[u] + cost[u][idx]
                    shortest[v] = 0
                    reachable[v] = 1

    # To mark all nodes reachable from negative cycles
    def bfs_negative_cycle(v):
        q = queue.Queue()
        q.put(v)
        visited = [False] * n
        visited[v] = True
        while not q.empty():
            u = q.get()
            shortest[u] = 0
            for idx, next_v in enumerate(adj[u]):
                if not visited[next_v]:
                    visited[next_v] = True
                    q.put(next_v)

    for u in range(n):
        if shortest[u] == 0:
            bfs_negative_cycle(u)

if __name__ == '__main__':
    #sys.stdin = open('input.txt', 'r')
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

