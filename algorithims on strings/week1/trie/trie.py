#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = dict()
    tree[0] = {}
    # write your code here
    n = 1
    for pattern in patterns:
        curr = 0
        for c in pattern:
            if c in tree[curr]:
                curr = tree[curr].get(c)
            else:
                tree[len(tree)] = {}
                tree[curr][c] = n
                curr = len(tree) - 1
                n += 1
    return tree


if __name__ == '__main__':
    #sys.stdin = open('input.txt', 'r')
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
