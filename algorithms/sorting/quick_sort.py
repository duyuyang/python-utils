# QuickSort

# Picks an element as pivot and partitions the given array around the picked pivot.
# partition(), given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x

def partition(arr, low, high):
  # choose the last element as pivot
  pivot = arr[high]

  # initiate the index of smaller element
  i = low - 1

  # loop from from low to high - 1
  for j in range(low, high):
    # if current el is <= pivot
    if arr[j] <= pivot:
      i += 1
      # swap arr[i] and arr[j]
      arr[i], arr[j] = arr[j], arr[i]
  
  # swap arr[i+1] and arr[high]
  arr[i+1], arr[high] = arr[high], arr[i+1]
  return i+1
  