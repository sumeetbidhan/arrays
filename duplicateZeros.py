class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                # Shift elements to the right starting from the end
                for j in range(len(arr) - 1, i, -1):
                    arr[j] = arr[j - 1]
                # Insert the duplicate zero
                if i + 1 < len(arr):
                    arr[i + 1] = 0
                # Move to the next element after the newly added zero
                i += 1
            # Move to the next element
            i += 1

# Example usage:
arr1 = [1, 0, 2, 3, 0, 4, 5, 0]
solution = Solution()
solution.duplicateZeros(arr1)
print(arr1)  # Output: [1, 0, 0, 2, 3, 0, 0, 4]

arr2 = [1, 2, 3]
solution.duplicateZeros(arr2)
print(arr2)  # Output: [1, 2, 3]
