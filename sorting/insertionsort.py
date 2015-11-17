# Iterators not supported
def insertionsort(arr):
  insertion = []
  for toinsert in arr:
    for i, value in enumerate(insertion):
      if toinsert < value:
        insertion.insert(i, toinsert)
        break
    else:
      insertion.append(toinsert)
  return insertion