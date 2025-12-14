/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // let arr = []
    // if (nums.length === 2){
    //     return [0, 1];
    // }
    // for (let i = 0; i < nums.length; i++){
    //     let a = nums[i];
    //     for (let j = 1; j < nums.length - 1; j++){
    //         let b = nums[j];
    //         if (nums[i] + nums[j] === target){
    //             arr.push(i);
    //             arr.push(j);
    //         } else {
    //             continue;
    //         }
    //     }
    // }
    // return arr
    let numMap = new Map(); 
    for (let i = 0; i < nums.length; i++) {
        let difference = target - nums[i];
        if (numMap.has(difference)) {
            return [numMap.get(difference), i];
        }
        numMap.set(nums[i], i);
    }
    return [];
};
