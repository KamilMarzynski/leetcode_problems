class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        for j in range(1, len(strs[0])+1):
            for i in range(1, len(strs)):
                if strs[i][0:j] != strs[0][0:j]:
                    return strs[0][0:j-1]
        
        return strs[0]