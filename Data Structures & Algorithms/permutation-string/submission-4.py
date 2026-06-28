from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        s1_count = Counter(s1)

        for i in range(len2 - len1 + 1):
            window = s2[i:i + len1]
            window_count = Counter(window)
            if window_count == s1_count:
                return True

        return False

    