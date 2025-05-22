/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    return function() {
        for (i = 0; i <= 2; i++) {
            sum = n++
            return sum
        };
    };
};
createCounter(10);
/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */
