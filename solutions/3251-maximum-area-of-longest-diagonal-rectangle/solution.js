/**
 * @param {number[][]} dimensions
 * @return {number}
 */
var areaOfMaxDiagonal = function(dimensions) {
    let output = []
    let max = -Infinity
    let maxArea = -Infinity
    for (let i = 0; i < dimensions.length; i++){
        output.push(Math.sqrt(dimensions[i][0]**2 + dimensions[i][1]**2));
    };
    for (let i = 0; i < output.length; i++){
        max = Math.max(output[i], max)
    };
    for (let i = 0; i < output.length; i++){
        let area = (dimensions[i][0] * dimensions[i][1])
        if (output[i] === max && area > maxArea){
            maxArea = area;
        };
    };
    return maxArea
};
