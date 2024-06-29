# python3
from math import inf

def build_heap(data):

    size = len(data) - 1
    swaps = []
    def get_parent(i):
        return (i - 1) // 2

    def get_left_child(i):
        return (i * 2) + 1

    def get_rigth_child(i):
        return (i * 2) + 2

    def shift_up(i):
        parent_idx = get_parent(i)
        if parent_idx == -1:
            return

        if data[parent_idx] <= data[i]:
            return

        while data[parent_idx] > data[i]:
            temp = data[parent_idx]
            data[parent_idx] = data[i]
            data[i] = temp
            parent_idx = get_parent(parent_idx)
            i = parent_idx

        return

    def shift_down(i):
        curr = i
        while curr < size:
            min_idx = curr
            left_child = get_left_child(curr)

            if left_child <= size and data[left_child] < data[min_idx]:
                min_idx = left_child

            rigth_child = get_rigth_child(curr)

            if rigth_child <= size and data[rigth_child] < data[min_idx]:
                min_idx = rigth_child


            if min_idx != curr:
                data[min_idx], data[curr] = data[curr], data[min_idx]
                swaps.append((curr, min_idx))
                curr = min_idx
            else:
                return

        return

    for i in range(len(data) // 2, -1, -1):
        shift_down(i)

    return swaps
    """
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps
    """

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
