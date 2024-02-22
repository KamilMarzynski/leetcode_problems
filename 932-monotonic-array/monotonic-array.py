class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        direction = ''
        for i in range(1, len(nums)):
            if direction is '':
                if nums[i] > nums[i-1]:
                    direction = 'asc'
                if nums[i] < nums[i-1]:
                    direction = 'desc'
            else:
                print(direction)
                if direction == 'asc' and nums[i] < nums[i-1]:
                    return False
                if direction == 'desc' and nums[i] > nums[i-1]:
                    return False
        
        return True
