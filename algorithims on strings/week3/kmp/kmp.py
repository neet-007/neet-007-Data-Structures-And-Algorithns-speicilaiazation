# python3
import sys


def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  s = pattern + '$' + text
  borders = [0] * len(s)

  border = 0
  for i in range(1, len(s)):
    while border > 0 and s[i] != s[border]:
      border = borders[border - 1]
    if s[i] == s[border]:
      border += 1
    else:
      border = 0

    borders[i] = border

  result = []

  for i in range(len(pattern) + 1, len(s)):
    if borders[i] == len(pattern):
      result.append(i - (2 * len(pattern)))

  # Implement this function yourself
  return result


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

