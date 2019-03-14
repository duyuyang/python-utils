from itertools import permutations

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
  # def twoSum(self, nums, target):
  #   def my_target(n):
  #     return n[0] + n[1] == target
  #   perm = set([tuple(sorted(e)) for e in permutations(nums, 2)])
  #   cl = []
  #   for i in filter(my_target, perm):
  #     cl.extend(list(i))
  #   result = []
  #   for i, v in enumerate(nums):
  #     for n in cl:
  #       if v == n:
  #         result.append(i)
  #         break
  #   return result

  # def twoSum(self, nums, target):
  #   # if target - num = a num:
  #   #    append to []
  #   col = []
  #   for i, n in enumerate(nums):
  #     gap = target - n

  #     if gap in nums[:i] or gap in nums[i+1:]:
  #       col.append(i)
  #   return col

  # def twoSum(self, nums, target):
  #   dicts = {}
  #   for i in range(0, len(nums)):
  #       x = nums[i]
  #       if x in dicts:
  #           return [dicts.get(x), i]
  #       dicts[target - x] = i

  def twoSum(self, nums, target):
    dicts = dict(zip(nums, range(len(nums))))
    # for i, v in dicts.iteritems():
    for v, i in dicts.items():
      gap = target - v
      if gap in nums[:i] or gap in nums[i+1:]:
        return [i, dicts[gap]]
  

if __name__ == '__main__':
  S = Solution()
  print(S.twoSum([2, 7, 11, 5], 9))
  # print(S.twoSum([3, 3], 6))
  print(S.twoSum([2, 7, 11, 5, 4, 6, 3, 6], 9))