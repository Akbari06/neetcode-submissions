class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        left = 0
        res = 0

        for right in range(len(s)):
            freq[s[right]] += 1
            no_unique = len(freq)

            while freq[s[right]] > 1:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left+=1

            res = max(res, right - left + 1)
        
        return res