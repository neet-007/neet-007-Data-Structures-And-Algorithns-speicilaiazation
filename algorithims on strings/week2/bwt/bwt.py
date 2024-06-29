# python3
import sys

def BWT(text):
    rotations = [text[i:] + text[:i] for i in range(len(text))]
    sorted_rotations = sorted(rotations)
    return "".join(row[-1] for row in sorted_rotations)

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))