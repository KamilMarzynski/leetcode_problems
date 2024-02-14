class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:        
        i = 0
        while n > 0 and i < len(flowerbed):
            if flowerbed[i] == 0:
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                if empty_left_plot and empty_right_lot:
                    flowerbed[i] = 1
                    n = n - 1
                    i = i + 1
            i = i + 1
            if n == 0:
                return True

        return n == 0