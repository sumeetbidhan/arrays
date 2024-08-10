public class Solution {
  public int pivotIndex(int[] nums) {
      int totalSum = 0, leftSum = 0;
      for (int num : nums) {
          totalSum += num;
      }
      for (int i = 0; i < nums.length; i++) {
          int rightSum = totalSum - leftSum - nums[i];
          if (rightSum == leftSum) {
              return i;
          }
          leftSum += nums[i];
      }
      return -1;
  }

  public static void main(String[] args) {
      int[] nums1 = {1, 7, 3, 6, 5, 6};
      Solution solution = new Solution();
      System.out.println(solution.ppivotIndex(nums1)); // Output: 3
  }
}
