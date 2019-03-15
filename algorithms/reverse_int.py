from collections import deque

# We want to repeatedly "pop" the last digit off of xx and "push" it to the back of the \text{rev}rev. In the end, \text{rev}rev will be the reverse of the xx.

class Solution(object):

    def reverse(self, x):
      stack = deque()
      init = 0
      flag = 1
      if x < 0:
        flag = -1
        x = abs(x)
      for i in reversed(range(len(str(x)))):
        init += x % 10 * (10 ** i)
        x = x // 10
      return init * flag



if __name__ == '__main__':
  s = Solution()
  print(s.reverse(123))
  print(s.reverse(-123))
  print(s.reverse(717))
  print(s.reverse(120))
  print(s.reverse(1534236469))