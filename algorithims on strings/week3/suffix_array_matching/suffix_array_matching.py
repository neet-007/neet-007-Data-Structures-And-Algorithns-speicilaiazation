# python3
import sys

def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  # Implement this function yourself

  mapper = {'$':0, 'A':1, 'C':2, 'G':3, 'T':4}
  def sort_chars():
    order = [-1] * len(text)
    count = [0] * 5

    for i in range(len(text)):
      count[mapper[text[i]]] += 1
    for i in range(1, len(count)):
      count[i] += count[i - 1]

    for i in range(len(text) - 1, -1, -1):
      count[mapper[text[i]]] -= 1
      order[count[mapper[text[i]]]] = i

    return order

  def compute_char_classes(order):
    class_ = [0] * len(text)
    class_[order[0]] = 0

    for i in range(1, len(text)):
      if text[order[i]] != text[order[i - 1]]:
        class_[order[i]] = class_[order[i - 1]] + 1
      else:
        class_[order[i]] = class_[order[i - 1]]

    return class_

  def doubles_sorting(order, class_, l):
    new_order = [-1] * len(text)
    count = [0] * len(text)

    for i in range(len(text)):
      count[class_[i]] += 1
    for i in range(1, len(count)):
      count[i] += count[i - 1]

    for i in range(len(text) - 1, -1, -1):
      start = (order[i] - l + len(text)) % len(text)
      cl = class_[start]
      count[cl] -= 1
      new_order[count[cl]] = start

    return new_order

  def updating_classes(order, l, class_):
    new_class_ = [0] * len(order)
    new_class_[order[0]] = 0

    for i in range(1, len(order)):
      curr, prev = order[i], order[i - 1]
      mid, prev_mid = (curr + l) % len(order), (prev + l) % len(order)

      if class_[curr] != class_[prev] or class_[mid] != class_[prev_mid]:
        new_class_[curr] = new_class_[prev] + 1
      else:
        new_class_[curr] = new_class_[prev]

    return new_class_

  result = sort_chars()
  class_ = compute_char_classes(result)

  l = 1
  while l < len(text):
    result = doubles_sorting(result, class_, l)
    class_ = updating_classes(result, l, class_)

    l = l * 2

  return result

def find_occurrences(text, patterns):
    occs = set()

    #write your code here

    def compare(p, t):
      i = 0
      while i < len(p) and i < len(t):
        if p[i] > t[i]:
          return False, 'b'
        if p[i] < t[i]:
          return False, 's'

        i += 1
      return True, 't'

    suffix_array = build_suffix_array(text)
    for pattern in patterns:
      lo = 0
      hi = len(suffix_array) - 1
      while lo < hi and hi < len(suffix_array):
        mid = lo + ((hi - lo) // 2)
        is_equal, dir_ = compare(pattern, text[suffix_array[mid]:len(text)])
        if len(pattern) < len(text) - suffix_array[mid] and is_equal:
          occs.add(suffix_array[mid])
          break

        if dir_ == 'b':
          lo = mid + 1
        else:
          hi = mid - 1

    return occs
if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    occs = find_occurrences(text, patterns)
    print(" ".join(map(str, occs)))