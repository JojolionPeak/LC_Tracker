/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    let total = 0
    for(let i = 0; i < s.length; i++){
        let val = s[i];
        if (val === 'M'){
            total+=1000;
        } else if (val === 'D'){
            total+=500;
        } else if (val === 'C' && (s[i+1] === 'D' || s[i+1] === 'M')){
            total-=100;
        } else if (val === 'C'){
            total+=100;
        } else if (val === 'L'){
            total+=50;
        } else if (val === 'X' && (s[i+1] === 'L' || s[i+1] === 'C')){
            total-=10;
        } else if (val === 'X'){
            total+=10;
        } else if (val === 'V'){
            total+=5;
        } else if (val === 'I' && (s[i+1] === 'X' || s[i+1] === 'V')){
            total-=1;
        } else if (val === 'I'){
            total+=1;
        }
    }
    return total;
};
