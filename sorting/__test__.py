from quicksort import quicksort
from selectionsort import selectionsort
from radixsort import radixsort
from insertionsort import insertionsort
from mergesort import mergesort
import random


def shuffled(arr):
  clone = arr[:]
  random.shuffle(clone)
  return clone


def inorder(arr):
  return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))


SORTERS = [
  quicksort,
  selectionsort,
  radixsort,
  insertionsort,
  mergesort
]


tests = [
  [],
  [1, 2, 3, 4],
  [4, 3, 2, 1],
  [4, 4, 2, 1],
  [1.24, 5.67, 3.45, -1.24],
  shuffled(list(range(0, 1000))),
  list(range(0, 1000)),
  (3, 4, 1, 2),
  (i for i in range(10, 0, -1))
]


if __name__ == '__main__':
  for sorter in SORTERS:
    print('SORTER: {}'.format(sorter.__name__))
    failures = 0

    for i, test in enumerate(tests):
      try:
        result = sorter(test)
        assert len(result) == len(test), 'length of result != length of input'
        assert inorder(result), 'result not in sorted ascending order'
      except Exception as e:
        print('\t!!! FAILED: Test #{}'.format(i+1))
        print('\t!!! ERROR: {}'.format(e))
        failures += 1
    
    if failures == 0:
      print('\tSUCCESS')
    else:
      print('\tFAILURES: {}'.format(failures))
