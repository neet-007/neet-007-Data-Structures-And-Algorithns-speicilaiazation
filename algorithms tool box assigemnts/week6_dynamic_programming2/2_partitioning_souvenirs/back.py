from sys import stdin
from itertools import combinations
from random import randint

def stress_test():
    while True:
        n = randint(1, 20)
        list_ = [0] * n
        for i in range(n):
            list_ [i] = randint(1, 30)
        print('test')
        print(list_)
        s_1 = partition_naive(list_)
        s_2 = partition3(list_)

        if s_1 != s_2:
            print(s_1)
            print(s_2)
            break

def find_subset_with_sum(values, target_sum):
    for l in range(1, len(values) + 1):
        for comp in combinations(values, l):
            if sum(comp) == target_sum:
                 return comp
    return None


def partition_naive(values: list[int]) -> int:
    total_sum = sum(values)
    if total_sum % 3 != 0:
        return 0
    
    target_sum = total_sum // 3
    subsets = []

    for _ in range(3):
        subset = find_subset_with_sum(values, target_sum)
        if subset is None:
            return 0
        subsets.append(subset)
        for val in subset:
            values.remove(val)

    return 1

def partition3(values:list[int]):
    if sum(values) % 3 != 0:
        return 0

    values.sort()
    sum_ = sum(values) / 3

    a = [[], [], []]
    index = len(values) - 1
    count = 0
    while len(values) > 0 and index >= 0:
        #print(index)
        a[count].append(values[index])
        sum_a = sum(a[count])
        if sum_a > sum_:
            a[count].pop()
            index -= 1
            continue

        values.pop(index)

        if sum_a == sum_:
            count += 1
            index = len(values) - 1
            continue

        index-= 1

    print(a)
    if count == 3:
        return 1

    return 0


if __name__ == '__main__':
    #input_n, *input_values = list(map(int, stdin.read().split()))
    #assert input_n == len(input_values)
    input_values = list(map(int, input().split()))
    print(partition3(input_values))
    #stress_test()
