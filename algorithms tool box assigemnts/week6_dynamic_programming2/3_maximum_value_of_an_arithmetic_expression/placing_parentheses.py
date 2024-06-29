from math import inf

def evaluate(a, b, op):
    a = int(a)
    b = int(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def min_max(i, j, min_d, max_d, dataset):
    max_ = -inf
    min_ = inf

    for k in range(i, j):
        op = 2 * k + 1

        a = evaluate(max_d[k][i], min_d[j][k + 1], dataset[op])
        b = evaluate(max_d[k][i], max_d[j][k + 1], dataset[op])
        c = evaluate(min_d[k][i], min_d[j][k + 1], dataset[op])
        d = evaluate(min_d[k][i], max_d[j][k + 1], dataset[op])

        min_ = min(min_, a, b, c, d)
        max_ = max(max_, a, b, c, d)

    return min_, max_

def maximum_value(dataset):
    n = (len(dataset) // 2) + 1

    min_d = [[0] * n for _ in range(n)]
    max_d = [[0] * n for _ in range(n)]

    for i in range(n):
        max_d[i][i] = int(dataset[i * 2])
        min_d[i][i] = int(dataset[i * 2])

    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            min_d[j][i], max_d[j][i] = min_max(i, j, min_d, max_d, dataset)

    return max_d[n - 1][0]


if __name__ == "__main__":
    print(maximum_value(input()))
