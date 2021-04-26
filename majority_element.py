from typing import List

class Solution:
    def majority_element_helper(self, nums, min, max):
        if (min == max):
            return nums[min]

        # recurse on left and right sides
        mid = (min + max) // 2
        left_nums = self.majority_element_helper(nums, min, mid)
        right_nums = self.majority_element_helper(nums, mid + 1, max)

        # if the two halves agree on the majority element, return it
        if (left_nums == right_nums):
            return left_nums

        # get counts
        left_nums_count = sum(1 for i in range(min, max + 1) if nums[i] == left_nums)
        right_nums_count = sum(1 for i in range(min, max + 1) if nums[i] == right_nums)

        if (left_nums_count > right_nums_count):
            return left_nums
        else:
            return right_nums


    def majorityElement(self, nums: List[int]) -> int:
        # EX input: [3, 3, 2] -> return 3
        # divide and conquer recursive method
        return self.majority_element_helper(nums, 0, len(nums) - 1)

if __name__ == "__main__":
    test1 = Solution()
    #test_arr = [3, 2, 3]
    #print(test1.majorityElement(test_arr))
