class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_len = len(nums)
        i = 0
        while i <= nums_len:
            while i < nums_len and nums[i] == val:
                nums.pop(i)
                nums_len = len(nums)
            i += 1

        return len(nums)