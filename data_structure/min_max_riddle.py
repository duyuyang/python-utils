import heapq
from collections import deque
# Given an integer array of size , find the maximum of the minimum(s) of every window size in the array. The window size varies from 1 to n.

def getMin(arr):
  heapq.heapify(arr)
  return heapq.nsmallest(1, arr)[0]

def getMax(arr):
  heapq.heapify(arr)
  return heapq.nlargest(1, arr)[0]

# def riddle(arr):
#   for i in range(len(arr)):
#     size = i + 1
#     winMins = deque()
#     for j in range(len(arr) - i):
#       winMins.append(getMin(arr[j:j+size]))
#     yield getMax(list(winMins))

def riddle(arr):
  stack = deque()
  max_window = {}
  # map number -> window size
  # Result: 
  # max_window: {1: 13, 2: 3, 3: 2, 4: 1, 7: 1}
  arr += [0,]
  # arr [2, 6, 1, 12, 0]
  for i, n in enumerate(arr):
    if not stack or n > stack[-1][1]:
      # stack is empty or the number > the number in the last set in stack
      # {(0, 2), (1, 6),}
      stack.append((i, n))
    else:
      while stack and stack[-1][1] >= n:
        # stack is not empty and the number in the last set in stack >= the number
        if i-stack[-1][0] not in max_window or max_window[i-stack[-1][0]] < stack[-1][1]:
          # (current index - index in the last set) not in max_window
          max_window[i-stack[-1][0]] = stack[-1][1]
          # max_window {1: 6, }
        p = stack.pop()
      stack.append((p[0], n))
  ans = [0]*(len(arr)-1)
  v_ant = min(max_window.values())

  print(max_window)
  for i in range(len(arr)-1, 0, -1):
    # Result:
    # [13, 3, 2, 1, 1, 1, 1]
    # [12, 2, 1, 1]
    if i in max_window and max_window[i] > v_ant:
      ans[i-1] = max_window[i]
      v_ant = max_window[i]
    else:
      ans[i-1] = v_ant
  return ans


if __name__ == '__main__':
  # print(list(riddle([1, 2, 3, 5, 1, 13, 3])))
  # print(list(riddle([2, 6, 1, 12])))
  print(list(riddle([11, 2, 3, 14, 5, 2, 11, 12])))
