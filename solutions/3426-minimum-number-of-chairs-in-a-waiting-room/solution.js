/**
 * @param {string} s
 * @return {number}
 */
var minimumChairs = function(s) {
    let count = 0;
    let avail = 0
    for (let i = 0; i < s.length; i++){
        console.log(count)
        console.log(s[i])
        if (s[i] === 'E'){
            avail++;
            if (count < avail) count++
        } else if (s[i] === 'L'){
            avail--;
        };
    };
    return count
};
