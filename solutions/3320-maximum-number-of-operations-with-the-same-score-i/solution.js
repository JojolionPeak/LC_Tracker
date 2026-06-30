/**
 * @param {number[]} nums
 * @return {number}
 */
var maxOperations = function(nums) {
    let count = 0
    let score = nums[0] + nums[1];
    do {
        nums.shift()
        nums.shift()
        count++
    } while (nums[0] + nums[1] === score);
    return count
};
