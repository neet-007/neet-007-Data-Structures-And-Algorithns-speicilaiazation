# python3
from collections import deque

def max_sliding_window_naive(sequence, m):
    maximums = []
    i = 0
    win_end = m - 1

    max_ = sequence[0]
    while i < len(sequence):
        if i == win_end:
            maximums.append(max_)
            win_end += 1
            max_ = sequence[i]
            continue

        if sequence[i] > max_:
            max_ = sequence[i]
        i += 1

    return maximums
    """
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums
    """

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

