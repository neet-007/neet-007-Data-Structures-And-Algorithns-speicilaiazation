#Uses python3
import sys
import math
import heapq

def weigth(x_1:int, x_2:int, y_1:int, y_2:int):
    return math.sqrt(((x_1 - x_2) ** 2) + ((y_1 - y_2) ** 2))

def minimum_distance(x:list[int], y:list[int]):
    #write your code here
    popped = set()
    results = 0

    heap = [[0, 0]]
    while len(popped) < len(x):
        cost, index = heapq.heappop(heap)
        if index in popped:
            continue
        popped.add(index)
        results += cost
        for i in range(len(x)):
            weigth_ = weigth(x[i], x[index], y[i], y[index])
            if not i in popped:
                heapq.heappush(heap, [weigth_, i])

    return results
if __name__ == '__main__':
    #sys.stdin = open('input.txt', 'r')
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
