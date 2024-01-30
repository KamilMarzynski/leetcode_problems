class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxAmountOfCandies = max(candies)
        result = []
        for candy in candies:
            result.append(candy + extraCandies >= maxAmountOfCandies)
        
        return result