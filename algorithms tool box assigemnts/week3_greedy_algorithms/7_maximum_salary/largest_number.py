from itertools import permutations

def largest_number_naive(numbers):
    """
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest
    """
    numbers.sort(reverse=True)
    sorted_numbers = numbers[0]
    for i in range(1, len(numbers)):
        sorted_numbers = str(max(int(sorted_numbers + numbers[i]), int(numbers[i] + sorted_numbers)))

    return int(sorted_numbers)

if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
