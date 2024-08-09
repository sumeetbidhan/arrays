class Solution {
  public void merge(int[] nums1, int m, int[] nums2, int n) {
      int i = m - 1; // Last element of the initialized part of nums1
      int j = n - 1; // Last element of nums2
      int k = m + n - 1; // Last position in nums1

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

  public static void main(String[] args) {
      Solution solution = new Solution();
      int[] nums1 = {1, 2, 3, 0, 0, 0};
      int m = 3;
      int[] nums2 = {2, 5, 6};
      int n = 3;
      solution.merge(nums1, m, nums2, n);
      for (int num : nums1) {
          System.out.print(num + " ");  // Output: 1 2 2 3 5 6
      }
  }
}
