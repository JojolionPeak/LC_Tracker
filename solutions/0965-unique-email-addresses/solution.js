/**
 * @param {string[]} emails
 * @return {number}
 */
var numUniqueEmails = function(emails) {
    const local = [];
    for (let i = 0; i < emails.length; i++){
        let [start, end] = emails[i].split('@')
        for ( let j = 0; j < start.length; j++){
            const char = start[j];
            start = start.replaceAll('.', '');
            if (char === '+'){
                let index = start.indexOf('+')
                start = start.slice(0,index);
            }
        }
        local.push(start+"@"+end);
    }
    console.log(local);
    const s = new Set(local)
    return s.size;
};
