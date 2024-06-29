def edit_distance(first_string, second_string):
    D = [[0] * (len(first_string) + 1) for _ in range(len(second_string) + 1)]

    for i in range(len(first_string) + 1):
        D[0][i] = i
    for j in range(len(second_string) + 1):
        D[j][0] = j

    for i in range(1, len(first_string) + 1):
        for j in range(1, len(second_string) + 1):
            insertion = D[j - 1][i] + 1
            deletion = D[j][i - 1] + 1
            matching = D[j - 1][i - 1]
            mismatching = D[j - 1][i - 1] + 1

            if first_string[i - 1] == second_string[j - 1]:
                D[j][i] = min(insertion, deletion, matching)
            else:
                D[j][i] = min(insertion, deletion, mismatching)

    return D[len(second_string)][len(first_string)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
