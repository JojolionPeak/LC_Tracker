/**
 * @param {number} n
 * @return {boolean}
 */
// const checkPower = (a) => {
//     let formula = Math.log(a)/Math.log(2)
//     console.log(formula)
//     if (formula !== Math.round(formula)){
//         return false;
//     }
//     return true;
// }
// var isPowerOfTwo = function(n) {
//     return checkPower(n);
// };
const isPowerOfTwo = (n) => {
        if (n === 0) return false;
        return Math.floor(Math.log2(n)) === Math.ceil(Math.log2(n));
    }
