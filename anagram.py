class Solution:
    '''
    Given two strings, returns true or false if they are anagrams.
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        return s == t 

