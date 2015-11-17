# Iterators not supported
def quicksort(arr):
  if len(arr) <= 1:
    return arr[:]
  pivot = arr[0]
  left = []
  right = []
  for item in arr[1:]:
    if item < pivot:
      left.append(item)
    else:
      right.append(item)
  return quicksort(left) + [pivot] + quicksort(right)