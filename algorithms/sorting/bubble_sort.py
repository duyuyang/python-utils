# Compare the first and the second element of the list and swap them if they are in wrong order.
# If there are n items in the list, then there are n−1 pairs of items that need to be compared on the first pass.
# It is important to note that once the largest value in the list is part of a pair, it will continually be moved along until the pass is complete.

class Solution(object):

  def bubble_sort(self, arr):
    for num in range(len(a)-1, 0, -1): # n-1 pairs
      for i in range(num): # for each pass, the largest number will be in the last
        if a[i] > a[i+1]:
          a[i+1], a[i] = a[i], a[i+1] # swap



if __name__ == '__main__':
  a = [11, 15, 3, 4, 9, -3]
  s = Solution()
  s.bubble_sort(a)
  print(a)