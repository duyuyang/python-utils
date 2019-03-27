def binarySearch(V, arr, l, r):
    # get the middle index
    m = l + (r - l) // 2
    if arr[m] == V:
      return m
    elif arr[m] > V:
        return binarySearch(V, arr, l, m-1)
    else:
        return binarySearch(V, arr, m+1, r)

m = binarySearch(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 0, 20)
print(m)