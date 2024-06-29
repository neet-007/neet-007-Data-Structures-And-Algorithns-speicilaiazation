def compute_operations(n):
    results = [[]] * (n + 1)
    results[1] = [1]

    for i in range(2, n + 1):
        results[i] = results[i - 1] + [results[i - 1][-1] + 1]

        if i % 2 == 0:
            temp = results[i // 2] + [results[i // 2][-1] * 2]
            if len(temp) < len(results[i]):
                results[i] = temp
        if i % 3 == 0:
            temp = results[i // 3] + [results[i // 3][-1] * 3]
            if len(temp) < len(results[i]):
                results[i] = temp

    return results[n]
if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
