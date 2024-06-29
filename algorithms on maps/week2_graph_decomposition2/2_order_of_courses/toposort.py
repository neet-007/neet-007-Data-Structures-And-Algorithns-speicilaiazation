#Uses python3

import sys

class stack():
    def __init__(self, len) -> None:
        self.arr = [-1] * len
        self.last = len - 1

    def push(self, val):
        if self.last < 0:
            return
        self.arr[self.last] = val
        self.last -= 1

def dfs(adj:list[list[int]], used:list[bool], order:stack, x:int):
    #write your code here
    if used[x]:
        return
    used[x] = True
    for neighbour in adj[x]:
        dfs(adj, used, order, neighbour)

    order.push(x)




def toposort(adj):
    used = [0] * len(adj)
    order = stack(len(adj))
    #write your code here
    for x in range(len(adj)):
        #used[x] = False
        dfs(adj, used, order, x)

    return order.arr

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
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

