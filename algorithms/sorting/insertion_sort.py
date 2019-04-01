# insert sort

def insertionSort1(n, arr):
  e = arr[n-1]
  while arr[n-2] > e and n > 1:
    arr[n-1] = arr[n-2]
    print(" ".join(map(str, arr)))
    n -= 1
  arr[n-1] = e
  print(" ".join(map(str, arr)))

arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
insertionSort1(10, arr)

# expect output
# 2 3 4 5 6 7 8 9 10 10
# 2 3 4 5 6 7 8 9 9 10
# 2 3 4 5 6 7 8 8 9 10
# 2 3 4 5 6 7 7 8 9 10
# 2 3 4 5 6 6 7 8 9 10
# 2 3 4 5 5 6 7 8 9 10
# 2 3 4 4 5 6 7 8 9 10
# 2 3 3 4 5 6 7 8 9 10
# 2 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 8 9 10
