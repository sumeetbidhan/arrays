class Solution {
  duplicateZeros(arr) {
      let i = 0;
      while (i < arr.length) {
          if (arr[i] === 0) {
              // Shift elements to the right starting from the end
              for (let j = arr.length - 1; j > i; j--) {
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
}

// Example usage:
const solution = new Solution();

let arr1 = [1, 0, 2, 3, 0, 4, 5, 0];
solution.duplicateZeros(arr1);
console.log(arr1); // Output: [1, 0, 0, 2, 3, 0, 0, 4]

let arr2 = [1, 2, 3];
solution.duplicateZeros(arr2);
console.log(arr2); // Output: [1, 2, 3]
