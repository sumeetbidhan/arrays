class Solution:
  def sortedSquares(self, nums: list[int]) -> list[int]:
    newNums = []
    for num in nums:
      num = num ** 2
      newNums.append(num)
    newNums= sorted(newNums)
    
    return newNums
  
squareList = [-4,-1,0,3,10]
solution = Solution()
print(solution.sortedSquares(squareList))