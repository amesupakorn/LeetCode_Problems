import re

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        
        sign = -1 if s[0] == '-' else 1
        s = s[1:] if s[0] in '+-' else s
        
        res = 0
        for ch in s:
            if not ch.isdigit():
                break
            res = res * 10 + (ord(ch) - ord('0'))
            
        return max(-2**31, min(sign * res, 2**31 - 1))