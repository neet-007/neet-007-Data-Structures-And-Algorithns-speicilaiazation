#Uses python3

import sys
import queue

def distance(adj, s, t):
    #write your code here
    dist = [float('inf')] * len(adj)
    dist[s] = 0
    queue_ = queue.Queue()
    queue_.put(s)
    while not queue_.empty():
        u = queue_.get()
        for neighbor in adj[u]:
            if dist[neighbor] != float('inf'):
                continue
            dist[neighbor] = dist[u] + 1
            queue_.put(neighbor)

    if dist[t] == float('inf'):
        return -1
    return dist[t]

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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
