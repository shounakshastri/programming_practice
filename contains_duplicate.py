# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
class Solution:
    def check_duplicate(self, nums: list[int]) -> bool:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                return True
            else:
                nums_dict[num] = 1
        return False
    
sol = Solution()
print(sol.check_duplicate([1,2,3,5,6]))
