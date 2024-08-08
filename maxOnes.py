class Solution:
  def findMaxConsecutiveOnes(self, nums):
    max_count = 0
    current_count = 0

    for num in nums:
      if num == 1:
        current_count +=1
      else: 
        max_count = max(max_count, current_count)
        current_count = 0

    max_count = max(max_count, current_count)

    return max_count
  

'''ones = [1,12,12,11,1,1,1,1,1,0,00,0,1,1,1,11,0,1,1,1,1,1,1,1,1,1,1,1,1,1]

print(Solution.findMaxConsecutiveOnes(None, ones))'''

# Create an instace of the solution classs
solution = Solution()

# Call the method on the instace
ones = [1,12,12,11,1,1,1,1,1,0,00,0,1,1,1,11,0,1,1,1,1,1,1,1,1,1,1,1,1,1]
print(solution.findMaxConsecutiveOnes(ones))
