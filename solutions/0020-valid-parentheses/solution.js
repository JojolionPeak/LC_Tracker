/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = [s[0]];
    for (let i = 1; i < s.length; i++){
        stack.push(s[i]);
        let last = stack[stack.length-1]
        let sec = stack[stack.length-2]
        if (last === ']' && sec === '[' || last === '}' && sec === '{' || last === ')' && sec === '(' ){
            stack.pop();           
            stack.pop();
        };
    };
    if (stack.length !== 0) return false
    return true
};
