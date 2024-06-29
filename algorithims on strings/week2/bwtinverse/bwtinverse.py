# python3
import sys

def InverseBWT(bwt):
    sorted_bwt = sorted([[bwt[i], i] for i in range(len(bwt))])
    index = sorted_bwt[0][1]
    s = ''

    while len(s) < len(bwt):
        s += sorted_bwt[index][0]
        index = sorted_bwt[index][1]

    return s

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))