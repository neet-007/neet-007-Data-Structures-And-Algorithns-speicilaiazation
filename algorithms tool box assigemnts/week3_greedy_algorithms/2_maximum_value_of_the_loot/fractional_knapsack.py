from sys import stdin

def get_best_item(weights, values):
    best_value = 0
    best_index = -1

    for i in range(len(weights)):
        if weights[i] > 0:
            current_value = values[i] / weights[i]
            if current_value > best_value:
                best_value = current_value
                best_index = i

    return best_index

def optimal_value(capacity, weights, values):
    value = 0

    while capacity > 0:
        best_index = get_best_item(weights, values)
        if best_index == -1:
            break  # No more items to consider

        fraction = min(weights[best_index], capacity)
        value += fraction * (values[best_index] / weights[best_index])
        weights[best_index] -= fraction
        capacity -= fraction

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
