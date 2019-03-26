

def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  
    # create temp arrays 
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    # Copy data to temp arrays L[] and R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     # Initial index of merged subarray 
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    # Copy the remaining elements of L[], if there 
    # are any 
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1

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