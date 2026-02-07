/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {

    let counter = {};
    nums.forEach((num) => {
        if (!counter[num]){
            counter[num] = 1;
        } else {
            counter[num]++;
        };
    });
    if (Object.values(counter).some(num => num > 1)){
        return true;
    }
    return false;
};
