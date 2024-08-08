class Solution:
  def findNumbers(self, nums: list[int]) -> int:
    even_number = 0
    for num in nums:
      num = str(num)

      if len(num) % 2 == 0:
        even_number += 1
    
    return even_number

nums = [555,901,482,1771]
solution = Solution()

print(solution.findNumbers(nums))