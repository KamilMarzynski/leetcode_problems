class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1[0] != str2[0]:
            return ''
        
        str1_length = len(str1)
        str2_length = len(str2)

        if str1_length > str2_length:
            shorter_input = str2
        else:
            shorter_input = str1

        for index in reversed(range(len(shorter_input) + 1)) : 
            if index == 0:
                return ''
            
            divisor_candidate = shorter_input[0:index]
            divisor_candidate_length = len(divisor_candidate)
    
            if str1_length % divisor_candidate_length == 0 and str2_length % divisor_candidate_length == 0 and str1_length // divisor_candidate_length * divisor_candidate == str1 and str2_length // divisor_candidate_length * divisor_candidate == str2:
                return divisor_candidate

        return ''            
