from math import inf
def change(money):
    # write your code here
    if money == 1:
        return 1
    min_num_coins = [0] * money
    coins = [1, 3, 4]
    for m in range(1, money):
        min_num_coins[m] = inf

        for c in coins:
            if m >= c:
                num_of_coins = min_num_coins[m - c] + 1

                if num_of_coins < min_num_coins[m]:
                    min_num_coins[m] = num_of_coins

    return min_num_coins[money - 1]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
