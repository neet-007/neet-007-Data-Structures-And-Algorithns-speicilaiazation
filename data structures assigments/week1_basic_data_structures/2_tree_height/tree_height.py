# python3

import sys
import threading
from typing import NamedTuple

class Node(NamedTuple):
    key:int
    children:list['Node']

def walk_tree(node:Node):

    a_ = []
    for child in node.children:
        a_.append(walk_tree(child))

    return 1 + max(a_) if len(a_) else 1
def compute_height(n, parents):
    # Replace this code with a faster implementation
    nodes = [Node(i, []) for i in range(n)]

    root = Node(-1, [])
    for i in range(n):
        parent_index = parents[i]
        if parent_index == -1:
            root = nodes[i]
        else:
            nodes[parent_index].children.append(nodes[i])

    return walk_tree(root)
    """
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height
    """
    return


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
