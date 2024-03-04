class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        
        i = 0
        j = len(needle)
        while j <= len(haystack):
            if needle == haystack[i:j]:
                return i
            i += 1
            j += 1
        return -1