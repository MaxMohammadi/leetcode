class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # essentially we are returning the length of the array without duplicates
        # brute force solution -> O(n^2)
        
        count = 0
        
        while count < len(nums) - 1:
            if nums[count] == nums[count + 1]:
                nums.remove(nums[count])
            else:
                count += 1
                
        return len(nums)
