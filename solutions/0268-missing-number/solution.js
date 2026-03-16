/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    const length = nums.length
    const sorted = nums.sort((a,b) => a - b);
    for (let i = 0; i < length; i++){
        if (nums[i] !== i){
            return i;
        }
    }
    return length;
};
