public class Solution {
  public int findNumbers(int[] nums){
    int evenNumber = 0;
    for (int num: nums){
      String numStr = Integer.toString(num);
      if (numStr.length() % 2 == 0){
        evenNumber++;
      }
    }
    return evenNumber;
  }
  
}

public static void main(String[] args){
  Solution solution = new Solution();
  int[] nums = {555, 901, 482, 1771};
  System.out.println(solution.findNumbers(nums))
}