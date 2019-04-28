class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0
        a = []
        
        for i in range(len(s)):
            for j in s[i:]:
                if j not in a:
                    a.append(j)
                    if len(a) > longest:
                        longest = len(a)
                else:
                    a = []
                    break
        return longest
