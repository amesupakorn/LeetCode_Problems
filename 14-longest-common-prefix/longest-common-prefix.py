class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        s1, s2 = min(strs), max(strs)
        for i, ch in enumerate(s1):
            if ch != s2[i]:
                return s1[:i]
        return s1