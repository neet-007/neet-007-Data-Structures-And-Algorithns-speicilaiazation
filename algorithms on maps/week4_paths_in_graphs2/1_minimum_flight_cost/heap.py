class InputException(Exception):
    def __init__(self, msg: str) -> None:
        # Initialize the base Exception class with the message
        super().__init__(msg)

class Node():
    def __init__(self, key, val, left=None, right=None, parent=None) -> None:
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class heap():
    def __init__(self, size) -> None:
        self.root = self.last = None
        self.elems = [Node] * size

    def create_node(self, key, val, left=None, right=None, parent=None):
        return Node(key, val, left, right, parent)

    def build_heap(self, arr:list[int], start:int):
        arr.sort()
        last = 0
        def partition(index:int) -> Node:
            nonlocal last
            i = index
            if index == 0:
                i = start
            if index == start:
                i = 0

            node = self.create_node(arr[index], i)
            if index == 0:
                self.root = node
            if i > last:
                last = i
                self.last = node
            if index * 2 + 1 <= len(arr) - 1:
                node.left = partition(index * 2 + 1)
                node.left.parent = node
            if index * 2 + 2 <= len(arr) - 1:
                node.right = partition(index * 2 + 2)
                node.right.parent = node

            self.elems[i] = node
            return node
        partition(0)


    def in_order(self, node:Node):
        if node.left:
            print('left')
            self.in_order(node.left)
        print('node')
        print(node.val)
        if node.right:
            print('right')
            self.in_order(node.right)

    def find(self, key:int) -> Node | None:
        curr = self.root
        last = None
        while curr:
            if curr.key == key:
                last = curr
                break
            if curr.key > key:
                curr = curr.left
            else:
                curr = curr.right

        return last

    def heapify_up(self, key:int=-1, node:Node | None=None):
        if key == -1 and not node:
            raise Exception()
        if key != -1:
            node = self.find(key)
            if not node:
                return

        while node.parent and node.parent.key > node.key:
            p = node.parent
            node.parent = p.parent
            if p.parent:
                if p.parent.left == p:
                    p.parent.left = node
                else:
                    p.parent.right = node

            p.parent = node
            l = node.left
            r = node.right
            if p.left == node:
                node.left = p
                node.right = p.right
                if p.right:
                    p.right.parent = node
            else:
                node.right = p
                node.left = p.left
                if p.left:
                    p.left.parent = node
            p.left = l
            if l:
                l.parent = p
            p.right = r
            if r:
                r.parent = p

            if node == self.last:
                self.last = p

    def heapify_down(self, key:int=-1, node:Node | None=None):
        if key == -1 and not node:
            raise InputException(f'key {key} and node {node} are invalind')
        if key != -1:
            node = self.find(key)
            if not node:
                return

        while True:
            p = node
            gc = None
            dir_ = ''
            if node.left and node.left.key < p.key:
                p = node.left
                gc = node.right
                dir_ = 'r'
            if node.right and node.right.key < p.key:
                p = node.right
                gc = node.left
                dir_ = 'l'
            if p == node:
                break

            p.parent = node.parent
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = p
                else:
                    node.parent.right = p
            else:
                self.root = p

            node.parent = p
            node.left = p.left
            if p.left:
                p.left.parent = node
            node.right = p.right
            if p.right:
                p.right.parent = node
            if dir_ == 'l':
                p.right = node
                p.left = gc
                if gc:
                    gc.parent = p
            if dir_ == 'r':
                p.left = node
                p.right = gc
                if gc:
                    gc.parent = p

            if p == self.last:
                self.last = node

    def change_last(self):
        successor = None
        if not self.last.parent:
            self.last = self.root = None
            return successor

        if self.last.parent.left and self.last.parent.left != self.last:
            successor = self.last.parent.left
        else:
            successor = self.last.parent
            successor.left = None
            successor.right = None

        self.last.parent.right = None
        self.last.parent = None
        return successor



    def min_(self) -> Node:
        return_val = self.root
        if not self.root:
            raise InputException('no root')

        """
        print('root')
        print(f'{self.root.val}, {self.root.key}')
        print('last')
        print(f'{self.last.val}, {self.last.key}')
        """
        if self.root == self.last:
            self.root = self.last = None
            return return_val

        self.last.left = self.root.left
        if self.root.left:
            self.root.left.parent = self.last
        self.last.right = self.root.right
        if self.root.right:
            self.root.right.parent = self.last
        self.root.left  = self.root.right = None

        self.root = self.last
        self.last = self.change_last()

        self.heapify_down(node = self.root)

        return return_val
    """
    def insert(self, key:int, val:int):
        node = self.create_node(key, val)
        if self.last.parent == self.root:
            self.last.left = node
            node.parent = self.last

        elif self.last.parent.right == node:
            if not self.last.parent.left.left:
                self.last.parent.left.left = node
                node.parent = self.last.parent.left.left
            else:
                self.last.parent.left.right = node
                node.parent = self.last.parent.left.right
        else:
            self.last.parent.right = node
            node.parent = self.last.parent

        self.last = node
        self.heapify_up(node=self.last)
"""

    def change_priority(self, key:int, new_key:int):
        node = self.elems[key]
        if not node:
            return

        node.key = new_key
        if key > new_key:
            self.heapify_up(node=node)
        elif key < new_key:
            self.heapify_down(node=node)

        #print(f'{node.key}, {node.val}, {node.left.val if node.left else ''}, {node.right.val if node.right else ''}')

    def empty(self):
        return True if not self.root else False