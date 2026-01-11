/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let curr = init;
    for(const num of nums) {
        curr = fn(curr, num)
    }

    return curr;
};