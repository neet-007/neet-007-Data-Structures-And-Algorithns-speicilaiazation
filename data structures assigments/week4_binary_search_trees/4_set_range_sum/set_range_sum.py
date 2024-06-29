# python3

from sys import stdin
from collections import deque

def print_tree(root):

    def tree_height(vertex):
        if not vertex:
            return 0
        return max(tree_height(vertex.left), tree_height(vertex.right)) + 1

    height = tree_height(root)
    level = 0
    spaces_reference = (2 ** (height + 1)) - 1

    nodes_remaining_in_level = 2 ** level
    nodes_missing = 0
    queue = deque([root])

    while queue:
        curr = queue.popleft()
        print(' ' * (spaces_reference // (2 ** level)), end='')
        print(curr.key)

        nodes_remaining_in_level -= 1
        if curr.left:
            queue.append(curr.left)
        else:
            nodes_missing += 1
        if curr.right:
            queue.append(curr.right)
        else:
            nodes_missing += 1

        if nodes_remaining_in_level < 1:
            level += 1
            nodes_remaining_in_level = (2 ** level) - nodes_missing
            nodes_missing = 0
            print('\n')

# Vertex of a splay tree
class Vertex:
  def __init__(self, key, sum, left, right, parent):
    (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)

def update(v):
  if v == None:
    return
  v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
  if v.left != None:
    v.left.parent = v
  if v.right != None:
    v.right.parent = v

def smallRotation(v):
  parent = v.parent
  if parent == None:
    return
  grandparent = v.parent.parent
  if parent.left == v:
    m = v.right
    v.right = parent
    parent.left = m
  else:
    m = v.left
    v.left = parent
    parent.right = m
  update(parent)
  update(v)
  v.parent = grandparent
  if grandparent != None:
    if grandparent.left == parent:
      grandparent.left = v
    else: 
      grandparent.right = v

def bigRotation(v):
  if v.parent.left == v and v.parent.parent.left == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  elif v.parent.right == v and v.parent.parent.right == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  else: 
    # Zig-zag
    smallRotation(v)
    smallRotation(v)

# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
  if v == None:
    return None
  while v.parent != None:
    if v.parent.parent == None:
      smallRotation(v)
      break
    bigRotation(v)
  return v

def get_predecessor(v):
    if v.left:
        current = v.left
        while current.right:
            current = current.right
        return current
    else:
        current = v
        while current.parent and current == current.parent.left:
            current = current.parent
        return current.parent

def get_successor(v):
    if v.right:
        current = v.right
        while current.left:
            current = current.left
        return current
    else:
        current = v
        while current.parent and current == current.parent.right:
            current = current.parent
        return current.parent

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key):
  v = root
  last = root
  next = None
  while v != None:
    if v.key >= key and (next == None or v.key < next.key):
      next = v
    last = v
    if v.key == key:
      break
    if v.key < key:
      v = v.right
    else:
      v = v.left
  root = splay(last)
  return (next, root)

def split(root, key):
  (result, root) = find(root, key)
  if result == None:
    return (root, None)
  right = splay(result)
  left = right.left
  right.left = None
  if left != None:
    left.parent = None
  update(left)
  update(right)
  return (left, right)


def merge(left, right):
  if left == None:
    return right
  if right == None:
    return left
  while right.left != None:
    right = right.left
  right = splay(right)
  right.left = left
  update(right)
  return right


# Code that uses splay tree to solve the problem

root = None

def insert(x):
  global root
  (left, right) = split(root, x)
  new_vertex = None
  if right == None or right.key != x:
    new_vertex = Vertex(x, x, None, None, None)
  root = merge(merge(left, new_vertex), right)
  #print_tree(root)

def erase(x):
  global root
  node, _ = find(root, x)

  if not node or node.key != x:
    return

  successor = get_successor(node)
  if not successor:
    if not node.parent:
      if node.left:
        node.left.parent = None
        root = node.left
        node.left = None
      else:
        root = None
      return

    if node.left:
       node.parent.right = node.left
       node.left.parent = node.parent
       node.parent = None
       node.left = None

       return

    node.parent.right = None
    node.parent = None

    return

  successor = splay(successor)
  node = splay(node)

  successor.left = node.left
  successor.parent = None
  if node.left:
    node.left.parent = successor

  root = successor

  if node.left:
    node.left = None
  if node.right:
    node.right = None

  # Implement erase yourself

def search(x):
  global root
  node, root = find(root, x)

  if node and node.key == x:
    return True

  return False

  # Implement find yourself

def sum(fr, to):
  global root
  (left, middle) = split(root, fr)
  (middle, right) = split(middle, to + 1)

  ans = 0
  # Complete the implementation of sum

  def traverse(vertex:Vertex):
    nonlocal ans
    if not vertex:
      return

    if vertex.key < fr:
      traverse(vertex.right)
      return

    traverse(vertex.left)
    ans += vertex.key
    traverse(vertex.right)

  traverse(middle)


  return ans

MODULO = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
  line = stdin.readline().split()
  if line[0] == '+':
    x = int(line[1])
    insert((x + last_sum_result) % MODULO)
  elif line[0] == '-':
    x = int(line[1])
    erase((x + last_sum_result) % MODULO)
  elif line[0] == '?':
    x = int(line[1])
    print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
  elif line[0] == 's':
    l = int(line[1])
    r = int(line[2])
    res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
    print(res)
    last_sum_result = res % MODULO