#Uses python3

import sys
import queue

def distance(adj:list[list[int]], cost:list[list[int]], s:int, t:int) -> int:
    #write your code here
    dist = [float('inf')] * len(adj)
    dist[s] = 0
    heap_ = queue.PriorityQueue()
    #heap_.build_heap(dist, s)
    for i in range(len(dist)):
        heap_.put([dist[i], i])

    while True:
        min_ = heap_.get()
        if min_[0] == float('inf'):
            break

        for neighbour in adj[min_[1]]:
            if dist[neighbour] > min_[0] + cost[min_[1]][adj[min_[1]].index(neighbour)]:
                dist[neighbour] =  min_[0] + cost[min_[1]][adj[min_[1]].index(neighbour)]
                #heap_.change_priority(neighbour, dist[neighbour])
                heap_.put([dist[neighbour], neighbour])
    if dist[t] == float('inf'):
        return -1
    return dist[t]


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
