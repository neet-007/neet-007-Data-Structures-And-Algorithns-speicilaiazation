# python3
import sys


mapper = {'$':0, 'A':1, 'C':2, 'G':3, 'T':4}
def PreprocessBWT(bwt):
  """
  Preprocess the Burrows-Wheeler Transform bwt of some text
  and compute as a result:
    * starts - for each character C in bwt, starts[C] is the first position
        of this character in the sorted array of
        all characters of the text.
    * occ_count_before - for each character C in bwt and each position P in bwt,
        occ_count_before[C][P] is the number of occurrences of character C in bwt
        from position 0 to position P inclusive.
  """
  # Implement this function yourself
  starts = [-1] * 5
  occ_counts_before = [[0] * 5 for _ in range(len(bwt) + 1)]
  sorted_bwt = sorted(bwt)

  starts[mapper[sorted_bwt[0]]] = 0
  for i in range(0, len(bwt)):
    idx = mapper[sorted_bwt[i]]
    idx_2 = mapper[bwt[i]]
    if starts[idx] == -1:
      starts[idx] = i
    occ_counts_before[i + 1] = occ_counts_before[i].copy()
    occ_counts_before[i + 1][idx_2] = occ_counts_before[i + 1][idx_2] + 1

  return starts, occ_counts_before

def CountOccurrences(pattern, bwt, starts, occ_counts_before):
  """
  Compute the number of occurrences of string pattern in the text
  given only Burrows-Wheeler Transform bwt of the text and additional
  information we get from the preprocessing stage - starts and occ_counts_before.
  """
  # Implement this function yourself
  top = 0
  bottom = len(bwt) - 1

  while top <= bottom:
    if len(pattern):
      last = pattern[-1]
      pattern = pattern[:-1]

      if last in bwt[top:bottom + 1]:
        idx = mapper[last]
        top = starts[idx] + occ_counts_before[top][idx]
        bottom = starts[idx] + occ_counts_before[bottom + 1][idx] - 1
      else:
        return 0
    else:
      return bottom - top + 1



if __name__ == '__main__':
  bwt = sys.stdin.readline().strip()
  pattern_count = int(sys.stdin.readline().strip())
  patterns = sys.stdin.readline().strip().split()
  # Preprocess the BWT once to get starts and occ_count_before.
  # For each pattern, we will then use these precomputed values and
  # spend only O(|pattern|) to find all occurrences of the pattern
  # in the text instead of O(|pattern| + |text|).
  starts, occ_counts_before = PreprocessBWT(bwt)
  occurrence_counts = []
  for pattern in patterns:
    occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
  print(' '.join(map(str, occurrence_counts)))
