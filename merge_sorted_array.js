class Solution {
  merge(nums1, m, nums2, n) {
      let i = m - 1; // Last element of the initialized part of nums1
      let j = n - 1; // Last element of nums2
      let k = m + n - 1; // Last position in nums1

      // while both arrays have elements to compare
      while (i >= 0 && j >= 0) {
          if (nums1[i] > nums2[j]) {
              nums1[k] = nums1[i];
              i--;
          } else {
              nums1[k] = nums2[j];
              j--;
          }
          k--;
      }

      // if nums2 has leftover elements, place them in nums1
      while (j >= 0) {
          nums1[k] = nums2[j];
          j--;
          k--;
      }
  }
}

// Example usage:
let nums1 = [1, 2, 3, 0, 0, 0];
let m = 3;
let nums2 = [2, 5, 6];
let n = 3;
let solution = new Solution();
solution.merge(nums1, m, nums2, n);
console.log(nums1);  // Output: [1, 2, 2, 3, 5, 6]
