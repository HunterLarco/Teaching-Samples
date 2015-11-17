from quicksort import quicksort
import random


def shuffled(arr):
  clone = arr[:]
  random.shuffle(clone)
  return clone


def inorder(arr):
  return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))


SORTERS = [
  quicksort
]


tests = [
  [],
  [1, 2, 3, 4],
  [4, 3, 2, 1],
  [4, 4, 2, 1],
  shuffled(list(range(0, 100))),
  (3, 4, 1, 2),
  (i for i in range(10, 0, -1))
]


if __name__ == '__main__':
  for sorter in SORTERS:
    print('Testing Sorter')
    failures = 0

    for i, test in enumerate(tests):
      try:
        result = SORTERS[0](test)
        assert len(result) == len(test)
        assert inorder(result)
      except Exception as e:
        print('\t!!! FAILED: Test #{}'.format(i+1))
        print('\t!!! ERROR: {}'.format(e))
        failures += 1
    
    if failures == 0:
      print('\tSUCCESS')
    else:
      print('\tFAILURES: {}'.format(failures))
