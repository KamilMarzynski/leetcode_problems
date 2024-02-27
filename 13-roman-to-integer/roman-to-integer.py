class Solution:
    def romanToInt(self, s: str) -> int:
        substractedValues = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']

        valuesLookup = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        res = 0
        for i in range(0, len(s)):
            if s[i:i+2] in substractedValues:
                res -= valuesLookup[s[i]]
            else:
                res += valuesLookup[s[i]]

        return res