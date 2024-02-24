class Solution:
    def isPalindrome(self, x: int) -> bool:
        i = 0
        strNum = str(x)
        j = len(strNum) - 1
        print(j)
        while i <= j:
            if strNum[i] != strNum[j]:
                return False
            i += 1
            j -= 1
        
        return True