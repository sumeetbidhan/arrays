class Solution {
  pivotIndex(nums) {
      let totalSum = nums.reduce((acc, num) => acc + num, 0);
      let leftSum = 0;

      for (let i = 0; i < nums.length; i++) {
          let rightSum = totalSum - leftSum - nums[i];
          if (rightSum === leftSum) {
              return i;
          }
          leftSum += nums[i];
      }
      return -1;
  }
}

const nums1 = [1, 7, 3, 6, 5, 6];
const solution = new Solution();
console.log(solution.pivotIndex(nums1)); // Output: 3
