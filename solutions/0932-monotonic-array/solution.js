/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isMonotonic = function(nums) {
    // let arr = [];
    // for (let i = 0; i < nums.length; i++){
    //     if (nums[i] > nums[i+1]){
    //         arr.push('desc');
    //     } else if (nums[i] < nums[i+1]){
    //         arr.push('asc');
    //     };
    // };
    // if (arr.every(x => x === arr[0])){
    //     return true;
    // };
    // return false;
    let hasInc = false;
    let hasDec = false;
    for (let i = 0; i < nums.length; i++){
        if (nums[i] > nums[i+1]){
            hasInc = true;
        } else if (nums[i] < nums[i+1]){
            hasDec = true;
        };
    };
    if (hasInc && hasDec){
        return false;
    };
    return true;
};
