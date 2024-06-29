# python3
import sys, threading

sys.setrecursionlimit(10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
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
         #print(f'root {start}')
         node = Node()
         node.start = start
         node.length = len(text) - start
         curr.next[mapper.get(text[start])] = node
         start += 1
         continue

      offset = start
      curr = curr.next[mapper.get(text[start])]
      while offset < len(text):
         matching_length = 1
         while offset + 1 < len(text) and matching_length < curr.length and text[offset + 1] == text[curr.start + matching_length]:
            matching_length += 1
            offset += 1
         #print(f'{start}, {offset}, {matching_length}, {curr.length}')
         #if start == 5:
         #   print(offset + matching_length)
         #   print(text[curr.length + matching_length])
         if matching_length < curr.length:
            #print(text[offset])
            node = Node()
            cuttoff = Node()
            node.start = offset + 1
            node.length = len(text) - node.start
            cuttoff.start = curr.start + matching_length
            cuttoff.length = curr.length - matching_length
            curr.length = matching_length
            cuttoff.next = curr.next
            curr.next = [NA] * 5
            curr.next[mapper.get(text[node.start])] = node
            curr.next[mapper.get(text[cuttoff.start])] = cuttoff
            break
         if matching_length == curr.length:
            if curr.next[mapper.get(text[offset + 1])] != NA:
               curr = curr.next[mapper.get(text[offset + 1])]
               offset += 1
               continue
            node = Node()
            node.start = offset + 1
            node.length = len(text) - node.start
            curr.next[mapper.get(text[node.start])] = node
            break
         curr = curr.next[mapper.get(text[offset])]

      start += 1

    stack = [tree]
    while len(stack):
       curr = stack.pop()
       if curr.start != NA:
         result.append(text[curr.start:curr.start + curr.length])
       for c in curr.next:
          if c != NA:
             stack.append(c)

    def print_node(node:Node):
       if node.start != NA:
          result.append(text[node.start:node.start + node.length])
       for n in node.next:
          if n != NA:
             print_node(n)

    #print_node(tree)
    return result
def main():
  #sys.stdin = open('input.txt', 'r')
  text = sys.stdin.readline().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))

threading.Thread(target=main).start()