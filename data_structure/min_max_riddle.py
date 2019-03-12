import heapq
from collections import deque
# Given an integer array of size , find the maximum of the minimum(s) of every window size in the array. The window size varies from 1 to n.

def getMinWindow(arr):
  heapq.heapify(arr)
  return heapq.heappop(arr)


def riddle(arr):
  maxlist = []

  for i in range(len(arr)):
    size = i + 1
    winMins = []
    for j in range(len(arr) - i):
      winMins.append(getMinWindow(arr[j:j+size]))
    maxlist.append(max(winMins))
  return maxlist
    

if __name__ == '__main__':
  print(riddle([1, 2, 3, 5, 1, 13, 3]))
