class Solution:
  def pivotIndex(self, nums: list[int]) -> int:
    totalSum = sum(nums)
    leftSum = 0

    for i in range(len(nums)):
      rightSum = totalSum - leftSum - nums[i]
      if rightSum == leftSum:
        return i
      leftSum +=nums[i]
    return -1
     


    
      

nums1 = [1, 7, 3, 6, 5, 6]
solution = Solution()
print(solution.pivotIndex(nums1))