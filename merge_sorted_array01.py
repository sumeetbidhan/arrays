class Solution:
  def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    # Start filling from the end of nums1
    i = m - 1 # Last element of the initialized part of nums1
    j = n - 1 # Last element of nums2
    k = m + n - 1 # Last position in nums1

    # while both arrays have elements to compare
    while i >= 0 and j >=0:
      if nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
      else:
        nums1[k] = nums2[j]
        j -= 1
      
      k -= 1

      # if nums2 has leftover elements, place them in nums1
      while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
      
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
solution = Solution()
solution.merge(nums1, m, nums2, n)
print(nums1) 