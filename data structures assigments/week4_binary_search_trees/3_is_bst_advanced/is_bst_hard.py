#!/usr/bin/python3
import sys, threading

sys.setrecursionlimit(10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
    if len(tree) < 1:
       return True

    def compare(vertex, left, right):
       if vertex == -1:
          return True

       if not(tree[vertex][0] < right and tree[vertex][0] >= left):
          return False

       return compare(tree[vertex][1], left, tree[vertex][0]) and compare(tree[vertex][2], tree[vertex][0], right)

    return compare(0, float('-inf'), float('inf'))

def IsBinarySearchTree_(tree):
    if len(tree) < 1:
       return True

    prev_ = [float('-inf'), 'l']

    def in_order_treverse(vertex, dir):
        a = True
        b = True

        if tree[vertex][1] != -1:
           a = in_order_treverse(tree[vertex][1], 'l')

        if tree[vertex][0] == prev_[0] and prev_[1] == 'l':
            return False

        if tree[vertex][0] < prev_[0]:
           return False

        prev_[0], prev_[1] = tree[vertex][0], dir

        if tree[vertex][2] != -1:
           b = in_order_treverse(tree[vertex][2], 'r')

        return a and b

    return in_order_treverse(0, 'r')

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
