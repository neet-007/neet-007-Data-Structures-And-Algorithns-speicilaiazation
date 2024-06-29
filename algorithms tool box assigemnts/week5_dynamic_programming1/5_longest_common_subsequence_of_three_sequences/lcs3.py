from pprint import pprint
def lcs3(first_sequence, second_sequence, third_sequence):
    D = [[[0] * (len(first_sequence) + 1) for _ in range(len(second_sequence) + 1)] for a in range(len(third_sequence) + 1)]

    for k in range(len(third_sequence) - 1, -1, -1):
        for j in range(len(second_sequence) - 1, -1, -1):
            for i in range(len(first_sequence) - 1, -1, -1):
                if first_sequence[i] == second_sequence[j] == third_sequence[k]:
                    D[k][j][i] = D[k + 1][j + 1][i + 1] + 1
                else:
                    D[k][j][i] = max(D[k + 1][j][i], D[k][j + 1][i], D[k][j][i + 1])


    return D[0][0][0]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
