class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = [0] * 26
        t_chars = [0] * 26

        for sc in s: s_chars[ord(sc) - ord('a')] += 1
        for tc in t: t_chars[ord(tc) - ord('a')] += 1 

        return s_chars == t_chars