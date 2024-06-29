def get_pisano_period_length(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
        # A Pisano Period starts with 01
        if previous == 0 and current == 1:
            return i + 1

def fibonacci_sum(n):
    n = n + 2
    # Getting the period
    pisano_period_length = get_pisano_period_length(10)
    # Taking mod of N with period length
    n = n % pisano_period_length
    # Calculating Fibonacci(N) % m
    previous, current = 0, 1
    if n <= 1:
        return n - 1  # F(n+2) - 1 becomes 0 - 1 = -1 if n == 0

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return (current - 1) % 10
    """
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10
    """

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
