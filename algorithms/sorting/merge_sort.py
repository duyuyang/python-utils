

def merge(arr, l, m, r):
  # assume left is sorted
  left = arr[l:m]
  # assume right is sorted
  right = arr[m+1:r]

def merge_sort(arr, l, r):
    if l < r:
        # if left < right index
        # devide list into half
        m = (l + r) // 2
        larr = arr[l:m]
        rarr = arr[m+1:r]
        # merge_sort the left half
        merge_sort(larr, l, m)
        # merge_sort the right half
        merge_sort(rarr, m+1, r)
        # merge the left and right
        merge(arr, l, m, r)

a = [12, 46, 2, 8, 11, 6, 7, 9, 17]

merge_sort(a, 0, len(a))

print(a)