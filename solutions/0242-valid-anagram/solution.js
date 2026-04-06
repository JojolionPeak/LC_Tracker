const isAnagram = (s, t) => {
    if(s.length !== t.length) {
        return false;
    }

    const sarr = s.split('').sort();
    const tarr = t.split('').sort();

    for (let i = 0; i < sarr.length; i++){
        if( sarr[i] !== tarr[i] ) return false;
    }
    return true;
}
