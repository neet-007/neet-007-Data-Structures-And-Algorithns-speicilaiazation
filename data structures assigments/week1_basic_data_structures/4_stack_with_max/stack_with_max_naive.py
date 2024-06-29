#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__order_stack = []

    def Push(self, a):
        self.__stack.append(a)
        self.__order_stack.append(a)
        self.__order_stack.sort(reverse=True)

    def Pop(self):
        assert(len(self.__stack))
        self.__order_stack.remove(self.__stack.pop())
        self.__order_stack.sort(reverse=True)

    def Max(self):
        assert(len(self.__stack))
        return self.__order_stack[0]

if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
