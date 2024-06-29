# python3
from random import randint


def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def poly_hash(s, x, p):
    hash_ = 0
    for i in range(len(s) - 1, -1, -1):
        hash_ = ((hash_ * x) + ord(s[i])) % p

    return hash_

def pre_computed_hashes(pattern, text, p, x):
    h = [0] * (len(text) - len(pattern) + 1)
    s = text[len(text) - len(pattern):]

    h[len(text) - len(pattern)] = poly_hash(s, x, p)

    y = 1
    for i in range(len(pattern)):
        y = (y * x) % p

    for i in range(len(text) - len(pattern) - 1, -1, -1):
        h[i] = ((x * h[i + 1]) + ord(text[i]) - (y * ord(text[i + len(pattern)]))) % p
        h[i] = (h[i] + p) % p

    return h

def get_occurrences(pattern, text):
    p = 800879
    x = randint(1, p - 1)
    positions = []
    p_hash = poly_hash(pattern, x, p)

    h = pre_computed_hashes(pattern, text, p, x)

    for i in range(0, len(text) - len(pattern) + 1):
        if p_hash != h[i]:
            continue

        if pattern == text[i:i + len(pattern)]:
            positions.append(i)

    return positions
    """
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if text[i:i + len(pattern)] == pattern
    ]
    """

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

