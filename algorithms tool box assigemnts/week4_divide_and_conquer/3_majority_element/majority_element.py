from math import floor
def majority_element_naive(elements):
    elements.sort()
    count = 0
    prev = elements[0]
    for e in elements:
        if e == prev:
            count += 1
        if count > (len(elements) / 2):
            return 1
        if e != prev:
            count = 1
            prev = e
            continue
    return 0
    """
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0
    """


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
