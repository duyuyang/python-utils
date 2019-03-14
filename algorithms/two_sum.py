from itertools import permutations

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
  def twoSum(self, nums, target):
    def my_target(n):
      return n[0] + n[1] == target
    perm = set([tuple(sorted(e)) for e in permutations(nums, 2)])
    cl = []
    for i in filter(my_target, perm):
      cl.extend(list(i))
    result = []
    for i, v in enumerate(nums):
      for n in cl:
        if v == n:
          result.append(i)
          break
    return result

if __name__ == '__main__':
  S = Solution()
  print(S.twoSum([2, 7, 11, 5], 9))
  print(S.twoSum([3, 3], 6))
