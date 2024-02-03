class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if(len(nums) < 3): return False
        first = inf
        second = inf
        for i in range(len(nums)):
          if nums[i] > second:
            return True
          elif nums[i] > first:
            second = nums[i]
          elif nums[i] < first:
            first = nums[i]

        return False