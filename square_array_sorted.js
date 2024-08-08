class Solution{
  sortedSquares(nums){
    let newNums = [];
    for (let num of nums){
      newNums.push(num * num);
    }
    newNums.sort((a, b) => a -b);
    return newNums
  }
}

const solution = new Solution();
const squareList = [-4, -1, 0, 3, 10];
console.log(soluton.sortedSquares(squareList));