/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    return function(...args) {
        return "Hello World"
    }
};
console.log(createHelloWorld(null));

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */
