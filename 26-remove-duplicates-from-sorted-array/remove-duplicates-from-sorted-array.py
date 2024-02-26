class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_len = len(nums)
        i = 1

        while i <= nums_len:
            while len(nums) > i and nums[i-1] == nums[i]:
                nums.pop(i)
            i += 1

        return len(nums)

        