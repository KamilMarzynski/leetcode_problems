class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 0  # Initialize the counter for unique elements.

        for i in range(1, len(nums)):
            # If the current element is not equal to the last unique element found,
            # increment k and update the next position with the current unique element.
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]

        # Return the number of unique elements, which is k + 1 because k is zero-based.
        return k + 1

        