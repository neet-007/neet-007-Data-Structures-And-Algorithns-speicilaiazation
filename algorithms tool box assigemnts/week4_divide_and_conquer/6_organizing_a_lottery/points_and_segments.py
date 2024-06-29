from sys import stdin


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)
    p_in_starts = [[]] * len(points)

    for i in range(len(points)):
        for j in range(len(starts)):
            if points[i] >= starts[j]:
                p_in_starts[i].append(j)

    for i in range(len(p_in_starts)):
        for j in range(len(p_in_starts[i])):
            if points[i] <= ends[p_in_starts[i][j]]:
                count[i] += 1
    """
    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1
    """
    return count


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover_naive(input_starts, input_ends, input_points)
    print(*output_count)
