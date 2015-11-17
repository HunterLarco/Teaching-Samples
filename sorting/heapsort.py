def getParent(index):
  return (index - 1) // 2

def getChildren(index):
  right = (index + 1) * 2
  left = right - 1
  return left, right

def getValue(arr, index):
  return arr[index] if index < len(arr) else None

def swap(arr, i1, i2):
  arr[i1], arr[i2] = arr[i2], arr[i1]

def fixUp(arr, index):
  if index == 0: return
  last = arr[index]
  parent = getParent(index)
  if arr[parent] > last:
    swap(arr, index, parent)
    fixUp(arr, parent)

def fixDown(heap, index):
  if len(heap) <= 1: return
  value = heap[index]
  left, right = getChildren(index)
  leftValue, rightValue = getValue(heap, left), getValue(heap, right)
  if leftValue != None and rightValue != None:
    largest = left if leftValue < rightValue else right
    if heap[largest] < value:
      swap(heap, index, largest)
      fixDown(heap, largest)
  elif leftValue != None and leftValue < value:
    swap(heap, index, left)
    fixDown(heap, left)
  elif rightValue != None and rightValue < value:
    swap(heap, index, right)
    fixDown(heap, right)

def heapify(arr):
  clone = arr[:]
  heap = []
  for item in clone:
    heap.append(item)
    fixUp(heap, len(heap)-1)
  return heap

def pop(heap):
  greatest = heap[0]
  heap[0] = heap[-1]
  del heap[-1]
  fixDown(heap, 0)
  return greatest

# Iterators not supported
def heapsort(arr):
  heap = heapify(arr)
  sort = []
  while heap:
    sort.append(pop(heap))
  return sort