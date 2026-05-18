# You are given an integer array nums of length n. 
# Create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed). 
# Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.
# 
# Example 1:
# Input: nums = [1,4,1,2]
# Output: [1,4,1,2,1,4,1,2]
# 
# Example 2:
# Input: nums = [22,21,20,1]
# Output: [22,21,20,1,22,21,20,1]
# Constraints:
# 1 <= nums.length <= 1000.
# 1 <= nums[i] <= 1000

class Solution:
    def getConcatanation(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(2):
            for a in nums:
                ans.append(a)
        return (ans)
    
    def getConcatenation_2(self, nums: list[int], num_of_copies: int) -> list[int]:
        ans = [0]*(len(nums) * num_of_copies)
        for i, num in enumerate(nums):
            ans[i] = ans[i+num_of_copies] = num
        return (ans)
    
    def getConcatanation_3(self, nums:list[int], num_of_copies=2) -> list[int]:
        return (nums*num_of_copies)

sol = Solution()
print(sol.getConcatanation(nums=[22,21,20,1]))