import heapq
from collections import deque
# Given an integer array of size , find the maximum of the minimum(s) of every window size in the array. The window size varies from 1 to n.

def getMin(arr):
  heapq.heapify(arr)
  return heapq.nsmallest(1, arr)[0]

def getMax(arr):
  heapq.heapify(arr)
  return heapq.nlargest(1, arr)[0]

def riddle(arr):
  for i in range(len(arr)):
    size = i + 1
    winMins = deque()
    for j in range(len(arr) - i):
      winMins.append(getMin(arr[j:j+size]))
    yield getMax(list(winMins))

if __name__ == '__main__':
  print(list(riddle([1, 2, 3, 5, 1, 13, 3])))
