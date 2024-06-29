def fibonacci_last_digit(n):
    if n <= 1:
        return n

    prev, current = 0, 1
    for _ in range(n - 1):
        prev, current = current, (prev + current) % 10

    return current

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
