/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    for (let i = digits.length; i--; i>=0) {
        const digit = digits[i]
        if(digit < 9) {
            digits[i] = digit + 1;
            return digits;
        } else {
            digits[i] = 0;
            if(i > 0) {
                continue;
            }
        }
        digits.unshift(1);
        return digits;
    }
};