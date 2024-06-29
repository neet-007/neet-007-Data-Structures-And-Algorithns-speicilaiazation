#!/usr/bin/python3
import sys, threading
import random
from pprint import pprint

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class BinaryTree():
    def __init__(self, size) -> None:
        self.size = size
        self.nodes = [[-1, -1, -1] for _ in range(size)]
        self.lower_bound = -2147483648
        self.upper_bound = 2147483648
        self.free_index = 0

    def partition(self, lo, hi):
        return ((hi - lo) // 2) + lo

    def arrange_bst(self, lo, hi, index):
        if lo > hi:
            return

        root_idx = ((hi - lo) // 2) + lo
        left_child_idx = (((root_idx - 1) - lo) // 2) + lo
        right_child_idx = ((hi - (root_idx + 1)) // 2) + (root_idx + 1)

        self.new_nodes[index][0] = self.nodes[root_idx][0]

        if left_child_idx >= lo and left_child_idx < root_idx:
            self.free_index += 1
            self.new_nodes[index][1] = self.free_index
            self.arrange_bst(lo, root_idx - 1, self.free_index)
        else:
            self.new_nodes[index][1] = -1

        if right_child_idx <= hi and right_child_idx > root_idx:
            self.free_index += 1
            self.new_nodes[index][2] = self.free_index
            self.arrange_bst(root_idx + 1, hi, self.free_index)
        else:
            self.new_nodes[index][2] = -1


    """
    def arrange_bst(self, lo, hi, index):
        if lo > hi or index >= self.size:
            return

        pivot_idx = self.partition(lo, hi)
        self.new_nodes[index][0] = self.nodes[pivot_idx][0]

        left_child_index = (2 * index) + 1
        right_child_index = (2 * index) + 2

        if left_child_index < self.size:
            self.new_nodes[index][1] = left_child_index
            self.arrange_bst(lo, pivot_idx - 1, left_child_index)
        else:
            self.new_nodes[index][1] = -1

        if right_child_index < self.size:
            self.new_nodes[index][2] = right_child_index
            self.arrange_bst(pivot_idx + 1, hi, right_child_index)
        else:
            self.new_nodes[index][2] = -1
    """

    def make_bst(self):
        set_ = set()
        while len(set_) < self.size:
            set_.add(random.randint(self.lower_bound, self.upper_bound))

        for i, num in enumerate(sorted(set_)):
            self.nodes[i][0] = num

        self.new_nodes = [[-1, -1, -1] for _ in range(self.size)]
        self.arrange_bst(0, self.size - 1, self.free_index)

        return self.new_nodes

    def make_tree(self):
      return


def stress_test():

  while True:
    print('test_start')
    size_ = random.randint(0, 1000000)
    bst = None
    #type_ = random.randint(0, 1)
    type_ = 0
    obj_ = BinaryTree(size_)
    if type_ == 0:
      bst = obj_.make_bst()
    #elif type_ == 1:
    #  bst = print(size_, True)
    val_1 = IsBinarySearchTree(bst)
    val_2 = IsBinarySearchTree_(bst)

    test = {
       'size':size_,
       'val1':val_1,
       'val2':val_2,
       'size':size_,
       'is_bst':type_,
       'bst':None
    }
    if val_1 != val_2:
       test['bst'] = bst
       pprint(test)
       break

    print('test_end')

def IsBinarySearchTree_(tree):
    def traverse_less(vertex, key):
        if vertex == -1:
            return True

        if tree[vertex][0] >= key:
            return False

        return traverse_less(tree[vertex][1], key) and traverse_less(tree[vertex][2], key)

    def traverse_more(vertex, key):
        if vertex == -1:
            return True

        if tree[vertex][0] <= key:
            return False

        return traverse_more(tree[vertex][1], key) and traverse_more(tree[vertex][2], key)

    for i in range(len(tree)):
        if tree[i][1] != -1:
            if not traverse_less(tree[i][1], tree[i][0]):
                return False
        if tree[i][2] != -1:
            if not traverse_more(tree[i][2], tree[i][0]):
                return False

    return True

def IsBinarySearchTree(tree):
    if len(tree) < 1:
        return True

    def compare(vertex, left, right):
        if vertex == -1:
            return True

        value = tree[vertex][0]
        left_child = tree[vertex][1]
        right_child = tree[vertex][2]

        if not (left < value < right):
            return False

        return compare(left_child, left, value) and compare(right_child, value, right)

    return compare(0, float('-inf'), float('inf'))


def main():
  #nodes = int(sys.stdin.readline().strip())
  #tree = []
  #for i in range(nodes):
  #  tree.append(list(map(int, sys.stdin.readline().strip().split())))
  #if IsBinarySearchTree(tree):
  #print("CORRECT")
  #else:
  # print("INCORRECT")

  stress_test()

threading.Thread(target=main).start()
