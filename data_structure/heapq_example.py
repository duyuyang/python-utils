# my understanding of heap

# heap seems to be a list but always being ordered in a way
# push will insert a new element to the list, then re-order
# pop will remove the smallest
# however, if you print out the list, it's not sorted


# Stack vs Heap Pros and Cons

# Stack
# very fast access
# don't have to explicitly de-allocate variables
# space is managed efficiently by CPU, memory will not become fragmented
# local variables only
# limit on stack size (OS-dependent)
# variables cannot be resized


# Heap
# variables can be accessed globally
# no limit on memory size
# (relatively) slower access
# no guaranteed efficient use of space, memory may become fragmented over time as blocks of memory are allocated, then freed
# you must manage memory (you're in charge of allocating and freeing variables)
# variables can be resized using realloc()



# Some Python code to demonstrate

# importing "heapq" to implement heap queue
import heapq

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print("The created heap is : ", end="")
print(list(li))

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li, 4)

# printing modified heap
print("The modified heap after push is : ", end="")
print(list(li))

# using heappop() to pop smallest element
print("The popped and smallest element is : ", end="")
print(heapq.heappop(li))

# using heappushpop() to push and pop items simultaneously
# pops 2
print("The popped item using heappushpop() is : ", end="")
print(heapq.heappushpop(li, 2))

# using heapreplace() to pop and push items simultaneously
# pops 3
print("The popped item using heapreplace() is : ", end="")
print(heapq.heapreplace(li, 2))

# using nlargest to print 3 largest numbers
# prints 10, 9 and 8
print("The 3 largest numbers in list are : ", end="")
print(heapq.nlargest(3, li))

# using nsmallest to print 3 smallest numbers
# prints 1, 3 and 4
print("The 3 smallest numbers in list are : ", end="")
print(heapq.nsmallest(3, li))


# problem:
# sort every element in the n x n matrix

# solution
# use heapq.merge to merge list into the 1st one
mat = [[10, 20, 30, 40],
       [15, 25, 35, 45],
       [27, 29, 37, 48],
       [32, 33, 39, 50]]

# move exeything into a list

from heapq import merge

result = mat[0]

for row in mat[1:]: # the rest of rows
  result = merge(result, row)

# result became an ordered generator
print(list(result))
# print(heapq.nlargest(3, result))


