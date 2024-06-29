def change(money):
    # write your code here
    number_of_coins = 0
    while money:
        if money >= 10:
            money -= 10
            number_of_coins += 1
        elif money >= 5:
            money -= 5
            number_of_coins += 1
        else:
            money -= 1
            number_of_coins += 1
    return number_of_coins


if __name__ == '__main__':
    m = int(input())
    print(change(m))
