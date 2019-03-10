import unittest

from collections import deque

# Problem:
# Check if the input brackets are balanced

# thinking:
# Use the collections.deque as a stack
# append the stack, pop the right once find the opposite
# In the end, the stack should be empty

def isBalanced(s):

  left = "([{"
  right = ")]}"
  br = dict(zip(right, left))
  
  my_stack = deque()

  if len(my_stack) % 2 != 0:
    return False
  for i in s:
    if i in left:
      my_stack.append(i)
    elif i in right:
      if not my_stack or my_stack.pop() != br.get(i):
        return False
  if len(my_stack) != 0:
    return False
  return True

class TestisBalanced(unittest.TestCase):

  def test_isBalanced(self):
    self.assertTrue(isBalanced("{[()]}"))
    self.assertTrue(isBalanced("{{[[(())]]}}"))
    self.assertFalse(isBalanced("{[(])}"))

  def test_isBalanced2(self):
    self.assertTrue(isBalanced("{(([])[])[]}"))
    self.assertFalse(isBalanced("{(([])[])[]]}"))
    self.assertTrue(isBalanced("{(([])[])[]}[]"))


if __name__ == '__main__':
  unittest.main()
