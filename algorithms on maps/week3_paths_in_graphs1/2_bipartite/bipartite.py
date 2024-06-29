#Uses python3

import sys
import queue
import random
from pprint import pprint
"""
def generate_random_bipartite_graph(num_vertices_set1, num_vertices_set2):
    adj_list = [[] for _ in range(num_vertices_set1 + num_vertices_set2)]

    for i in range(num_vertices_set1):
        for j in range(num_vertices_set1, num_vertices_set1 + num_vertices_set2):
            if random.choice([True, False]):
                adj_list[i].append(j)
                adj_list[j].append(i)

    return adj_list

def generate_random_non_bipartite_graph(num_vertices):
    adj_list = [[] for _ in range(num_vertices)]

    # Generate random edges
    for _ in range(num_vertices):
        u, v = random.sample(range(num_vertices), 2)
        adj_list[u].append(v)
        adj_list[v].append(u)

    # Ensure the graph is non-bipartite by introducing an odd-length cycle
    if num_vertices >= 3:
        u, v, w = random.sample(range(num_vertices), 3)
        adj_list[u].append(v)
        adj_list[v].append(u)
        adj_list[v].append(w)
        adj_list[w].append(v)
        adj_list[w].append(u)
        adj_list[u].append(w)

    return adj_list


def stress_test():
    while True:
        print('tets start')
        num_vertices = random.randint(0, 20)
        choice = random.randint(0, 1)
        type_ = 'bi'
        graph = None
        if choice == 0:
            type_ = 'normal'
            graph = generate_random_non_bipartite_graph(num_vertices)
        else:
            graph = generate_random_bipartite_graph(num_vertices // 2, num_vertices - (num_vertices // 2))

        res = bipartite(graph)
        if res != choice:
            test = {
                'num_vertice':num_vertices,
                'type':type_,
                'graph':graph,
                'choice':choice,
                'res':res
            }
            pprint(test)
            break
        print('test end')
"""


def bipartite(adj):
    #write your code here
    teams = [-1] * len(adj)
    queue_ = queue.Queue()

    for i in range(len(adj)):
        if teams[i] != -1:
            continue
        queue_.put(i)
        teams[i] = 0
        while not queue_.empty():
            u = queue_.get()
            for neighbour in adj[u]:
                if teams[neighbour] == -1:
                    teams[neighbour] = 0 if teams[u] == 1 else 1
                    queue_.put(neighbour)
                elif teams[neighbour] == teams[u]:
                    return 0

    #print(teams)
    return 1

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
    print(bipartite(adj))
    #stress_test()
