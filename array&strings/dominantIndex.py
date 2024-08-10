class Solution:
  def dominantIndex(self, nums: list[int]) -> int:
    for i in range(len(nums)):
      if nums[i + 1] > nums[i ]:
        doubleNums = nums[i + 1] ** 2
        if doubleNums <= nums[i]:
          return i
    return -1
  


solution = Solution()
print(solution.dominantIndex([3, 6, 1, 0]))  # Output: 1
print(solution.dominantIndex([1, 2, 3, 4]))  # Output: -1