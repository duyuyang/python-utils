# my understanding of heap

## heap seems to be a list but always being ordered in a way
## push will insert a new element to the list, then re-order
## pop will remove the smallest


# Some Python code to demonstrate
  
# importing "heapq" to implement heap queue 
import heapq 
  
# initializing list 
li = [5, 7, 9, 1, 3] 
  
# using heapify to convert list into heap 
heapq.heapify(li) 
  
# printing created heap 
print ("The created heap is : ",end="") 
print (list(li)) 
  
# using heappush() to push elements into heap 
# pushes 4 
heapq.heappush(li,4) 
  
# printing modified heap 
print ("The modified heap after push is : ",end="") 
print (list(li)) 
  
# using heappop() to pop smallest element 
print ("The popped and smallest element is : ",end="") 
print (heapq.heappop(li)) 

# using heappushpop() to push and pop items simultaneously 
# pops 2 
print ("The popped item using heappushpop() is : ",end="") 
print (heapq.heappushpop(li, 2)) 
  
# using heapreplace() to pop and push items simultaneously 
# pops 3 
print ("The popped item using heapreplace() is : ",end="") 
print (heapq.heapreplace(li, 2)) 

# using nlargest to print 3 largest numbers 
# prints 10, 9 and 8 
print("The 3 largest numbers in list are : ",end="") 
print(heapq.nlargest(3, li)) 
  
# using nsmallest to print 3 smallest numbers 
# prints 1, 3 and 4 
print("The 3 smallest numbers in list are : ",end="") 
print(heapq.nsmallest(3, li)) 