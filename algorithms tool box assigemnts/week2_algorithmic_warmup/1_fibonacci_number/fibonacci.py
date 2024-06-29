def fibonacci_number(n):
    fibonacci_list = [None] * (n + 1)
    fibonacci_list[0] = 0
    if n > 0:
        fibonacci_list[1] = 1
        for i in range(2, n + 1):
            fibonacci_list[i] = fibonacci_list[i - 1] + fibonacci_list[i - 2]

    return fibonacci_list[-1]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
