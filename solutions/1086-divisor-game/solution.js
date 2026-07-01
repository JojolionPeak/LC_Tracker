/**
 * @param {number} n
 * @return {boolean}
 */
var divisorGame = function(n) {
    let moveCount = 0;
    let subtract = 0;
    do {
        if (subtract !== 0){
            n -= subtract;
            subtract = 0
        }
        if (subtract === 0) {
            for (let i = 1; i < n; i++){
                if (n % 1 === 0){
                    subtract = i;
                    break;
                };
            };
        };
        moveCount++;

    } while (n > 1);
    if (moveCount % 2 === 0){
        return true;
    };
    return false;
};
