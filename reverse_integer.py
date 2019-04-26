'''
Given a 32-bit signed integer, reverse digits of an integer.

Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1 
        s = str(x)
        x_ = int(s[::-1].strip('-'))
        if x_ == 0 or x_ > 2**31-1:
            return 0
        else:
            return x_*sign

