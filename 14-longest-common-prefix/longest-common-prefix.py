class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort()
        word1 = strs[0]
        wordl = strs[-1]

        lcp = ''
        for c in range(len(word1)):
            if word1[c] == wordl[c]:
                lcp+=word1[c]
            else:
                break
        return lcp