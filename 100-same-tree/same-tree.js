/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    const traverse = function*(node, side = 'root') {
        if(!node) {
            return;
        }
        yield [node.val, side];

        if(node.left) {
            yield* traverse(node.left, 'left');
        } else {
            yield [null, 'left']
            yield* traverse(node.right, 'right');
        }
        if (node.right) {
            yield* traverse(node.right, 'right');
        }
    }

    const qTraverse = traverse(q);
    const pTraverse = traverse(p);
    
    for (const [value, side] of pTraverse) {
        const next = qTraverse.next();
        if(next.done) {
            return false;
        }
        
        const [qvalue, qside] = next.value;
        if(qvalue !== value || qside !== side) {
            return false;
        }
    }

    return qTraverse.next().done && pTraverse.next().done;
};