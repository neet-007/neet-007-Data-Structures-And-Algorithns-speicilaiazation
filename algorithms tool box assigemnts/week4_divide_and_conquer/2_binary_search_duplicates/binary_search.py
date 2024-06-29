from math import floor
def helper(hey, needle):
    lo = 0
    hi = len(hey) - 1
    return_value = -1
    while lo <= hi:
        mid = lo + floor((hi - lo) / 2)
        if hey[mid] == needle:
            return_value = mid
            break
        if needle > hey[mid]:
            lo = mid + 1
            continue
        hi = mid - 1

    if return_value == -1:
        return return_value

    while hey[return_value] == needle and return_value >= 0:
        return_value-= 1

    return return_value + 1



def binary_search(keys, query):
    # write your code here
    return helper(keys, query)

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
