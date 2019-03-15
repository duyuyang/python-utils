# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true
# Example 2:

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

from collections import deque

class Solution(object):
    # def isPalindrome(self, x):
    #   stack = deque()
    #   stack.extend(list(str(x)))
    #   if x < 0:
    #     return False
    #   for i in range(len(stack)//2):
    #     if stack.pop() != stack.popleft():
    #       return False
    #   return True

    def isPalindrome(self, x):
        x = str(x)
        if x[::-1] == x: # 1234 -> 4321
            return True
        else:
            return False


if __name__ == '__main__':
  s = Solution()
  print(s.isPalindrome(1221))
  print(s.isPalindrome(12321))
  print(s.isPalindrome(-12321))
  print(s.isPalindrome(123241))