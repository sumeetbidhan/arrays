import java.util.Arrays;

public class Solution{
  public int[] sortedSquares(int[] nums){
    int[] newNums = new int[nums.length];
    for (int i = 0; i < nums.length; i++){
      newNums[i] = nums[i] * nums[i];
    }
    Arrays.sort(newNums);
    return newNums;
  }

  public static void main(String[] args){
    Solution solution = new Solution();
    int[] squareList = {-4, -1, 0, 3, 10};
    int[] result = solution.sortedSquares(squareList);
    System.out.println(Arrays.toString(result));
  }
  
}
