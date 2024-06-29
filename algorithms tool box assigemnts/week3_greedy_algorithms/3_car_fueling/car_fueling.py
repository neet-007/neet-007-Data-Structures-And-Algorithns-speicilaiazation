from sys import stdin

def get_best_stop(tank, stops, last_stop):
    best_index = 0
    best_stop = 0
    for i in range(len(stops)):
        if (stops[i] - last_stop) <= tank:
            best_index = i
            best_stop = stops[i]
    stops = stops[best_index + 1:]
    return best_stop, stops

def min_refills(distance, tank, stops):
    # write your code here
    number_of_stops = 0
    last_stop = 0
    while len(stops) > 0:
        if distance <= tank:
            return number_of_stops
        best_stop, stops = get_best_stop(tank=tank, stops=stops, last_stop=last_stop)
        distance -= (best_stop - last_stop)
        last_stop = best_stop
        number_of_stops += 1

    if distance <= tank:
        return number_of_stops

    return -1


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    #d = int(input('d'))
    #m = int(input('m'))
    #stops = list(map(int, input('stops').split()))
    print(min_refills(d, m, stops))
