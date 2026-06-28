class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        left = 0
        n = len(s)
        res = 0
        most_freq = 0

        for right in range(n):
            freq[s[right]] += 1
            most_freq = max(most_freq, freq[s[right]])

            while (right - left + 1) - most_freq > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            res = max(res, right - left + 1)

        return res