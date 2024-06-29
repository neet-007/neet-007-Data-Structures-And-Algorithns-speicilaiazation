# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def recurse_in_order(self, vetrex):

     if self.left[vetrex] != -1:
        self.recurse_in_order(self.left[vetrex])

     self.result.append(self.key[vetrex])

     if self.right[vetrex] != -1:
        self.recurse_in_order(self.right[vetrex])

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.recurse_in_order(0)
    return self.result

  def recurse_pre_order(self, vertex):
    self.result.append(self.key[vertex])

    if self.left[vertex] != -1:
      self.recurse_pre_order(self.left[vertex])

    if self.right[vertex] != -1:
       self.recurse_pre_order(self.right[vertex])

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.recurse_pre_order(0)

    return self.result

  def recurse_post_order(self, vertex):
    if self.left[vertex] != -1:
      self.recurse_post_order(self.left[vertex])

    if self.right[vertex] != -1:
       self.recurse_post_order(self.right[vertex])

    self.result.append(self.key[vertex])

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that

    self.recurse_post_order(0)

    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
