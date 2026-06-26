/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let str = String(x);
    let arr = [];

    for (let i = str.length-1; i >= 0; i--){
        arr.push(str[i]);
    };

    arr = arr.join('');

    if (Number(arr) === x){
        return true;
    };

    return false;
};
