#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int totalSum = 0, leftSum = 0;
        for (int num : nums) {
            totalSum += num;
        }
        for (int i = 0; i < nums.size(); i++) {
            int rightSum = totalSum - leftSum - nums[i];
            if (rightSum == leftSum) {
                return i;
            }
            leftSum += nums[i];
        }
        return -1;
    }
};

int main() {
    vector<int> nums1 = {1, 7, 3, 6, 5, 6};
    Solution solution;
    cout << solution.pivotIndex(nums1) << endl; // Output: 3
    return 0;
}
