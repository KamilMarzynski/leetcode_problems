class Solution:
    def isValid(self, s: str) -> bool:
        openings = ['(', '[', '{']
        mapping = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        queue = []

        for parentheses in s:
            if parentheses in openings:
                queue.append(parentheses)
            else:
                if len(queue) == 0:
                    return False

                to_compare = queue.pop()
                if mapping[to_compare] != parentheses:
                    return False
        
        return len(queue) == 0