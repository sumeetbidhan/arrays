class Solution:
  def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    nums3 = []

    for i in range(m):
      nums3.append(nums1[i])
    
    for j in range(n):
      nums3.append(nums2[j])

    nums3.sort()

    for k in range(len(nums3)):
      nums1[k] = nums3[k]

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
solution = Solution()
solution.merge(nums1, m, nums2, n)
print(nums1) 