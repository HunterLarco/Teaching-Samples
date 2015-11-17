from collections import defaultdict
from math import log10, ceil

def charLength(number):
  if number == 0:
    return 1
  return int(ceil(log10(number)))

def charFromEnd(number, i):
  return int(abs(number) / 10**i % 10)

# positive numbers only
def radixsort(arr):
  if arr == []: return []
  clone = arr[:]
  maxint = max(clone)
  maxlen = charLength(maxint)
  for index in range(maxlen):
    bins = defaultdict(list)
    for item in clone:
      char = charFromEnd(item, index)
      bins[char].append(item)
    clone = [item for char in range(10) for item in bins[char]]
  return clone