class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def findMiddle(start: int, end: int):
            middle = (start + end) // 2

            if (start > end):
                return start

            if nums[middle] < target:
                return findMiddle(middle + 1, end)
            elif nums[middle] > target:
                return findMiddle(start, middle - 1)
            else:
                return middle
            
        return findMiddle(0, len(nums) - 1) 

