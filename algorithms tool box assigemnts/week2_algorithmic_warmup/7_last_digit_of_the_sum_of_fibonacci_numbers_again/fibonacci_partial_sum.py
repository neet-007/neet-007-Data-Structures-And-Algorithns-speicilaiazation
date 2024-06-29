# Uses python3
import sys

def get_pisano_period_length(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1

def fibonacci_mod(n, m):
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m
    return current

def fibonacci_sum_last_digit(n):
    pisano_period_length = get_pisano_period_length(10)
    n = (n + 2) % pisano_period_length
    last_digit = fibonacci_mod(n, 10)
    return (last_digit - 1) % 10

def fibonacci_partial_sum_naive(from_, to):
    if from_ == 0:
        sum_to = fibonacci_sum_last_digit(to)
        return sum_to
    
    sum_to = fibonacci_sum_last_digit(to)
    sum_from_minus_one = fibonacci_sum_last_digit(from_ - 1)
    
    result = sum_to - sum_from_minus_one
    if result < 0:
        result += 10

    return result


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
