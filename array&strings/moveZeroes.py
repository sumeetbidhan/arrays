class Solution:
  def moveZeroes(self, nums: list[int]) -> None:
    new_list = []
    i = 0
    for num in nums:
      if num == 0:
        i +=1
      else:
        new_list.append(num)
    
    while i > 0:
      new_list.append(0)
      i -= 1
    print(new_list)
    j = 0 
    for num in new_list:
      nums[j] = new_list[j]
      j += 1