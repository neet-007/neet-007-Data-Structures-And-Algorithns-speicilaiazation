from sys import stdin

def maximum_gold(capacity, weights):
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + weights[i])

    return dp[capacity]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    #input_capacity = int(input())
    #input_weights = list(map(int, input().split()))
    print(maximum_gold(input_capacity, input_weights))
