# python3
import sys

NA = -1

class Node:
	def __init__ (self):
		self.c = None
		self.next = [NA] * 4
		self.is_leaf = False

def solve (text, n, patterns):
	result = []
	trie = Node()
	mapper = {'a':0, 'g':1, 'c':2, 't': 3}
	def build_trie():
		for pattern in patterns:
			curr = trie
			for c in pattern:
				if curr.next[mapper.get(c.lower())] != NA:
					curr = curr.next[mapper.get(c.lower())]
				else:
					new_node = Node()
					new_node.c = c
					curr.next[mapper.get(c.lower())] = new_node
					curr = new_node
			curr.is_leaf = True

	build_trie()

	def prefix_trie_matching(count):
		s = count
		v = trie
		res = NA
		while True:
			if v.is_leaf:
				if res != NA:
					result.append(res)
				break
			if s < len(text) and v.next[mapper.get(text[s].lower())] != NA:
				if res == NA:
					res = s
				v = v.next[mapper.get(text[s].lower())]
				s += 1
			else:
				break
	#write your code here
	count = 0
	while count < len(text):
		prefix_trie_matching(count)
		count += 1
	return result

#sys.stdin = open('input.txt', 'r')
text = sys.stdin.readline().strip()
n = int (sys.stdin.readline().strip())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')
