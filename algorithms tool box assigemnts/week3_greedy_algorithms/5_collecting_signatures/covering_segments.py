from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments:list[Segment]):
    print(segments)
    points = [[] for _ in range(len(segments) * 2)]
    # write your code here
    for i in range(0, len(segments) - 1, 2):
        print(i)
        print(i + 1)
        for s_ in segments:
            if s_.start <= segments[i].start or segments[i].start <= s_.end:
                points[i].append(s_)
            if s_.start <= segments[i].end or segments[i].end <= s_.end:
                points[i + 1].append(s_)

    return points


if __name__ == '__main__':
    #input = stdin.read()
    #n, *data = map(int, input.split())
    #segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    input_ = input().split()
    segments = []
    for i in range(0, len(input_) - 1, 2):
        segments.append(Segment(int(input_[i]), int(input_[i + 1])))

    points = optimal_points(segments)
    print(len(points))
    #print(*points)
