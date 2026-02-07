/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (x < 0){
        return false;
    } else {
        let str = x.toString();
        let test = []
        for (let i = str.length - 1; i > -1; i--){
            (test.push(str[i]));
        };
        console.log(test);
        if (x === Number(test.join(''))){
            return true;
        }
    }
    return false;
};
