class Solution:
  def duplicateZeros(self, arr: list[int]) -> None:
    # First, count the number of zeros in the array
    zeros = arr.count(0)
    n = len(arr)

    # We iterate backward through the array 
    for i in range(n-1, -1, -1):
      if i + zeros < n:
        arr[i + zeros] = arr[i]
      if arr[i] == 0:
        zeros -= 1
        if i + zeros < n:
          arr[i + zeros] = 0

# Example usage:
arr1 = [1,0,2,3,0,4,5,0]
solution = Solution()
solution.duplicateZeros(arr1)
print(arr1)  # Output: [1,0,0,2,3,0,0,4]

arr2 = [1,2,3]
solution.duplicateZeros(arr2)
print(arr2)  # Output: [1,2,3]