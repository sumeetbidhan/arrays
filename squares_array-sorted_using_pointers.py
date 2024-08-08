class Solution:
  def sortedSquares(self, nums: list[int]) -> list[int]:
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    index = n - 1

    while left <= right:
      if abs(nums[left]) > abs(nums[right]):
        result[index] = nums[left] ** 2
        left +=1

      else:
        result[index] = nums[right] ** 2
        right -= 1 
      index -= 1

    return result
  
squareList = [-4, -1, 0, 3, 10]
solution = Solution()
print(solution.sortedSquares(squareList))
