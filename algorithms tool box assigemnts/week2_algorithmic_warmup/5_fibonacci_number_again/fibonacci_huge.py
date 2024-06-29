def get_pisano_period_length(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m

        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1

def fibonacci_huge_naive(n, m):
    # Getting the period
    pisano_period_length = get_pisano_period_length(m)
    # Taking mod of N with period length
    n = n % pisano_period_length
    # Calculating Fibonacci(N) % m
    previous, current = 0, 1
    if n <= 1:
        return n

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
