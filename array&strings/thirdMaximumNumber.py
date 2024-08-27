class Solution:
  def thirdMax(self, nums: list[int]) -> int:
    mySet = set(nums)
    mySet = sorted(mySet, reverse=True)

    n = len(mySet)
    for i in range(n):
      if n >= 3:
        return mySet[2]
    else:
      return max(mySet)