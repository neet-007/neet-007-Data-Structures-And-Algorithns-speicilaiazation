#Uses python3

import sys
import random

def negative_cycle(adj, cost):
    #write your code here
    distance=[0]*len(adj)
    distance[0] = 0
    for ind in range(len(adj)):
        for u in range(len(adj)):
            for v in adj[u]:
                v_index = adj[u].index(v)
                if distance[v] > distance[u] + cost[u][v_index]:
                    distance[v] = distance[u] + cost[u][v_index]
                    if ind==len(adj) - 1:
                        return 1
    return 0
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
    print(negative_cycle(adj, cost))
