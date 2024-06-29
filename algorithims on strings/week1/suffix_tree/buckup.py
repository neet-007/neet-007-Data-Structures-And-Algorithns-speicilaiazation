# python3
import sys

NA = -1

class Node():
  def __init__(self) -> None:
    self.next = [NA] * 5
    self.start = -1
    self.length = 0

def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding
    substrings of the text) in any order.
    """
    result = []
    tree = Node()
    mapper = {'A':0, 'T':1, 'G':2, 'C':3, '$':4}
    start = 0
    while start < len(text):
      curr = tree
      if curr.next[mapper.get(text[start])] == NA:
         node = Node()
         node.start = start
         node.length = len(text) - start
         curr.next[mapper.get(text[start])] = node
         start += 1
         continue

      offset = start
      curr = curr.next[mapper.get(text[start])]
      while offset + 1 < len(text) and curr.next[mapper.get(text[offset + 1])] != NA:
         offset += 1
         curr = curr.next[mapper.get(text[offset])]

      external = Node()
      external.start = offset + 1
      external.length = len(text) - external.start
      if curr.length == 1:
         curr.next[mapper.get(text[external.start])] = external
         start += 1
         continue
      cuttoff = Node()
      cuttoff.start = curr.start + 1
      cuttoff.length = curr.length - 1
      curr.length = 1
      while text[external.start] == text[cuttoff.start]:
         node = Node()
         node.start = curr.start + 1
         node.length = 1
         external.start += 1
         external.length -= 1
         cuttoff.start += 1
         cuttoff.length -= 1
         curr.next[mapper.get(text[node.start])] = node
         curr = node
      curr.next[mapper.get(text[external.start])] = external
      curr.next[mapper.get(text[cuttoff.start])] = cuttoff

      start += 1
    def print_node(node:Node):
       if node.start != NA:
          result.append(text[node.start:node.start + node.length])
       for n in node.next:
          if n != NA:
             print_node(n)

    print_node(tree)
    return result
if __name__ == '__main__':
  sys.stdin = open('input.txt', 'r')
  text = sys.stdin.readline().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))