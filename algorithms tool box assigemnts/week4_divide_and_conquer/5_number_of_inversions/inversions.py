from itertools import combinations
from math import floor

def merge(A:list[int], B:list[int]):
    results = []
    while len(A) > 0 and len(B) > 0:
        a = A[0]
        b = B[0]

        if a <= b:
            results.append(A[0])
            A = A[1:]
        else:
            results.append(B[0])
            B = B[1:]

    for i in range(len(A)):
        results.append(A[i])
    for i in range(len(B)):
        results.append(B[i])

    return results

def merge_sort(a, count):
    if len(a) == 1:
        return a, count

    p = floor(len(a) / 2)
    A, count_a = merge_sort(a[:p], count)
    B, count_b = merge_sort(a[p:], count)

    i, j, count = 0 , 0, 0
    while i < len(A) and j < len(B):
        if A[i] > B[j]:
            count += 1
        i += 1
        j += 1
    count += count_a + count_b
    array = merge(A, B)

    return array, count

def inversions_naive(a):
    _, count = merge_sort(a, 0)
    return count
    """
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions
    """

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(inversions_naive(elements))
