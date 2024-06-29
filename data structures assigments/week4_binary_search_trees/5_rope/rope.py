# python3

import sys

class Node():
	def __init__(self, key, left=None, right=None, parent=None) -> None:
		self.key = key
		self.left= left
		self.right = right
		self.parent = parent

class Rope:
	def __init__(self, s):
		self.s = s
		self.root = None
		self.ns = ''

	def create_node(self, key, left=None, right=None, parent=None):
		return Node(key, left, right, parent)

	def build(self) -> None:
		if len(self.s) < 1:
			self.ns = ''
			return

		root_idx = len(self.s) // 2
		self.root = self.create_node(self.s[root_idx])

		def traverse(node:Node, lo, hi, dir):
			if lo > hi:
				return

			new_node_idx = ((hi - lo) // 2) + lo
			new_node = self.create_node(self.s[new_node_idx])

			new_node.parent = node
			if dir == 'l':
				node.left = new_node
			else:
				node.right = new_node

			traverse(new_node, lo, new_node_idx - 1, 'l')
			traverse(new_node, new_node_idx + 1, hi, 'r')

		traverse(self.root, 0, root_idx - 1, 'l')
		traverse(self.root, root_idx + 1, len(self.s) - 1, 'r')

	def in_order_traverse(self, node:Node) -> None:
		if node == None:
			return

		self.in_order_traverse(node.left)
		self.ns += node.key
		self.in_order_traverse(node.right)

	def in_order_traverse_with_count(self, node: Node, count: list, goal: int, flag=False) -> Node | None:
		if goal >= len(self.ns):
			return None
		# Traverse the left subtree
		if node.left:
			result = self.in_order_traverse_with_count(node.left, count, goal, flag)
			if result:
				return result

		# Increment the count
		if flag:
			print(count)
			print(goal)
		count[0] += 1
		if count[0] == goal:
			return node

		# Traverse the right subtree
		if node.right:
			result = self.in_order_traverse_with_count(node.right, count, goal, flag)
			if result:
				return result

		return None

	def zig(self, root: Node, node: Node) -> tuple[Node, Node]:
		parent = node.parent
		if not parent:
			return root, node

		if parent.left == node:
			parent.left = node.right
			if node.right:
				node.right.parent = parent
			node.right = parent
		else:
			parent.right = node.left
			if node.left:
				node.left.parent = parent
			node.left = parent

		node.parent = parent.parent
		if parent.parent:
			if parent.parent.left == parent:
				parent.parent.left = node
			else:
				parent.parent.right = node
		parent.parent = node

		if root == parent:
			root = node
		return root, node

	def rotation(self, root: Node, node: Node) -> tuple[Node, Node]:
		parent = node.parent
		if not parent:
			return root, node
		grandparent = parent.parent
		if not grandparent:
			return self.zig(root, node)

		if grandparent.left == parent and parent.left == node:
			root, parent = self.zig(root, parent)
			root, node = self.zig(root, node)
		elif grandparent.right == parent and parent.right == node:
			root, parent = self.zig(root, parent)
			root, node = self.zig(root, node)
		else:
			root, node = self.zig(root, node)
			root, node = self.zig(root, node)

		return root, node

	def splay(self, root: Node, node: Node) -> Node:
		while root != node:
			root, node = self.rotation(root, node)
		return node

	def split(self, root:Node, node:Node):
		node = self.splay(root, node)

		right = node.right
		node.right = None

		if right:
			right.parent = None

		return node, right

	def merge(self, root:Node, left:Node, right:Node):
		if not left:
			return right
		if not right:
			return left

		while right.left:
			right = right.left
		right = self.splay(root, right)
		right.left = left

		return right

	def get_successor(self, node:Node) -> Node | None:
		if not node:
			return None

		curr = node.right

		if not curr:
			curr = node
			while curr.parent and curr.parent.right == curr:
				curr = curr.parent
			return curr.parent

		while curr.left:
			curr = curr.left

		return curr

	def delete(self, root:Node, node:Node) -> tuple[Node | None, Node]:
		successor = self.get_successor(node)

		if not successor:
			if node.parent:
				node.parent.right = node.left
				if node.left:
					node.left.parent = node.parent
			else:
				root = node.left

			node.parent = None
			node.left = None

			return root, node

		if not node.left and not node.right:
			if node.parent:
				if node.parent.left == node:
					node.parent.left = None
				else:
					node.parent.right = None
			else:
				root = None
			node.parent = None

			return root, node

		l = successor.right
		p = successor.parent
		successor.parent = node.parent
		if node.parent:
			if node.parent.left == node:
				node.parent.left = successor
			else:
				node.parent.right = successor
		else:
			root = successor

		successor.right = node.right
		if node.right:
			node.right.parent = successor

		p.left = l
		if l:
			l.parent = p

		return root, node

	def result(self):
		return self.ns

	def process(self, i, j, k):
        # Write your code here
		split_text, _ = self.split(self.root, self.in_order_traverse_with_count(self.root, [-1], j))
		_, split_text = self.split(split_text, self.in_order_traverse_with_count(split_text, [-1], i))

		k_node = self.in_order_traverse_with_count(self.root, [-1], k, True)
		print(k_node.key)
		k_node = self.splay(self.root, k_node)

		def traverse(root:Node, node:Node, count:list[int]):
			root_ = None
			if node.left:
				root_ = traverse(root, node.left, count)

			if i <= count[0] or count[0] <= j:
				root_temp, _ = self.delete(root_ if root_ else root, node)
				if root_temp:
					root_ = root_temp

			if node.right:
				root_temp = traverse(root, node.right, count)
				if root_temp:
					root_ = root_temp

			return root_ if root_ else root

		#k_node = traverse(k_node, k_node, [0])
		before, after = self.split(k_node, k_node)
		before = self.merge(split_text, before, split_text)
		after = self.merge(after, before, after)

		self.root = after
		self.in_order_traverse(self.root)

rope = Rope(sys.stdin.readline().strip())
rope.build()
rope.in_order_traverse(rope.root)

q = int(sys.stdin.readline())
for _ in range(q):
	i, j, k = map(int, sys.stdin.readline().strip().split())
	rope.process(i, j, k)
	print(rope.result())
