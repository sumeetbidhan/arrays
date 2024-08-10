import java.util.Arrays;

class Solution {
    public void duplicateZeros(int[] arr) {
        int i = 0;
        while (i < arr.length) {
            if (arr[i] == 0) {
                // Shift elements to the right starting from the end
                for (int j = arr.length - 1; j > i; j--) {
                    arr[j] = arr[j - 1];
                }
                // Insert the duplicate zero
                if (i + 1 < arr.length) {
                    arr[i + 1] = 0;
                }
                // Move to the next element after the newly added zero
                i++;
            }
            // Move to the next element
            i++;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[] arr1 = {1, 0, 2, 3, 0, 4, 5, 0};
        solution.duplicateZeros(arr1);
        System.out.println(Arrays.toString(arr1)); // Output: [1, 0, 0, 2, 3, 0, 0, 4]

        int[] arr2 = {1, 2, 3};
        solution.duplicateZeros(arr2);
        System.out.println(Arrays.toString(arr2)); // Output: [1, 2, 3]
    }
}
