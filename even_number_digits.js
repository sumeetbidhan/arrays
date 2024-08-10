class Solution{
  findNumbers(nums){
    let evenNumbers = 0;

    for (let num of nums){
      let numStr = num.toString();
      if (numStr.length % 2 === 0){
        evenNumbers++;
      }
    }
    return evenNumbers;
  }
}

const solution = new Solution();
const nums = [555, 901, 482, 1771];
console.log(solution.findNumbers(nums));