def optimal_summands(n):
    summands = []
    sum_ = 0

    for i in range(1, n + 1):
        if sum_ + i > n:
            break
        sum_ += i
        summands.append(i)

    if sum_ != n:
        summands[-1] = summands[-1] + (n - sum_)

    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
