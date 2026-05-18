# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# 
# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true
# 
# Example 2:
# Input: s = "jar", t = "jam"
# Output: false
# 
# Constraints: 
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.

class Solution:
    def is_anagram(self, s=str, t=str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = {}
        t_dict = {}

        for idx in range(len(s)):
            s_dict[s[idx]] = s_dict.get(s[idx], 0) + 1
            t_dict[t[idx]] = t_dict.get(t[idx], 0) + 1

        # for c in s:
        #     if c in s_dict:
        #         s_dict[c] += 1
        #     else:
        #         s_dict[c] = 1

        # for c in t:
        #     if c in t_dict:
        #         t_dict[c] += 1
        #     else:
        #         t_dict[c] = 1

        return s_dict == t_dict
    
sol = Solution()
print(sol.is_anagram("racecar", "carapace"))