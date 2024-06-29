from itertools import permutations


def max_dot_product(first_sequence, second_sequence):
    """"
    max_product = 0
    for permutation in permutations(second_sequence):
        dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
        max_product = max(max_product, dot_product)
    """
    first_sequence.sort()
    second_sequence.sort()

    return sum(first_sequence[i] * second_sequence[i] for i in range(len(first_sequence)))

if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))

