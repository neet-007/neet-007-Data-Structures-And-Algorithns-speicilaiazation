from random import randint


def partition3(array, left, right):
    pivot = left
    prev_index = left

    while left < right:
        if array[left + 1] < array[pivot]:
            prev_index += 1
            array[prev_index], array[left + 1] = array[left + 1], array[prev_index]

        left += 1

    array[pivot], array[prev_index] = array[prev_index], array[pivot]
    after_index = prev_index
    pivot = prev_index + 1
    while pivot < right:
        if array[pivot] == array[prev_index]:
            after_index += 1
            array[after_index] , array[pivot] = array[pivot], array[after_index]

        pivot += 1
    return prev_index, after_index
    # write your code here


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
