'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        '''
        2-15, Solution is base on discuss Post, and Lagou course
        '''
        longest = 0
        left, right = 0,0 # two bound for substring
        chars = set()   #store possible sub string, no-duplicate
        
        ##need two pointers to loop through all char in string, and 
        ##for the loop to terminate, need two pointer point to last char
        
        while left < len(s) and right < len(s):
            if s[right] not in chars:
                chars.add(s[right])
                right += 1
                longest = max(longest, right - left)
            else:
                chars.remove(s[left])
                left += 1
        
        return longest
                

        
    
   
