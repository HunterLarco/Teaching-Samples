def mergesort(arr):
  if len(arr) <= 1:
    return arr
  half = len(arr) // 2
  left = arr[:half]
  right = arr[half:]
  left = mergesort(left)
  right = mergesort(right)
  return merge(left, right)


def merge(arr1, arr2):
  combined = []
  while arr1 and arr2:
    if arr1[0] < arr2[0]:
      combined.append(arr1[0])
      arr1 = arr1[1:]
    else:
      combined.append(arr2[0])
      arr2 = arr2[1:]
  combined += arr1 + arr2
  return combined