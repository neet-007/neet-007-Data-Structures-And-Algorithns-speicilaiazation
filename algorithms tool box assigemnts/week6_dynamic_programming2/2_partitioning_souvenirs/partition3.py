from sys import stdin

def partition3(values:list[int]):
    sum_ = sum(values)
    if sum_ % 3 != 0:
        return 0

    values.sort(reverse=True)
    target = sum_ // 3
    used = [False] * len(values)

    def backtrace(i, k, subset_sum):
        if k == 0:
            return 1
        if subset_sum == target:
            return backtrace(0, k - 1, 0)

        for j in range(i, len(values)):
            if used[j] or subset_sum + values[j] > target:
                continue

            used[j] = 1

            if backtrace(j + 1, k, subset_sum + values[j]):
                return 1

            used[j] = 0

        return 0

    return backtrace(0, 3, 0)

if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    #input_values = list(map(int, input().split()))
    print(partition3(input_values))

