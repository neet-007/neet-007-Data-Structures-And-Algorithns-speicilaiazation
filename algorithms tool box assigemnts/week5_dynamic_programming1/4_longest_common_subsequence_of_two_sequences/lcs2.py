from pprint import pprint
def lcs2(first_sequence, second_sequence):
    D = [[0] * (len(first_sequence) + 1) for _ in range(len(second_sequence) + 1)]


    for j in range(len(second_sequence) - 1, -1, -1):
        for i in range(len(first_sequence) - 1, -1, -1):
            if first_sequence[i] == second_sequence[j]:
                D[j][i] = D[j + 1][i + 1] + 1
            else:
                D[j][i] = max(D[j + 1][i], D[j][i + 1])

    return D[0][0]
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
