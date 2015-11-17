# Iterators not supported
def selectionsort(arr):
  selection = []
  clone = list(arr)
  while clone:
    smallest = min(clone)
    selection.append(smallest)
    clone.remove(smallest)
  return selection
