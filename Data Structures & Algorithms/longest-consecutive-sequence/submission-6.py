class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        new = sorted(set(nums))
        counter = 1
        max_streak = 1

        for x in range(len(new)):
            if x != (len(new) - 1):
                if (new[x+1] - new[x] == 1):
                    counter += 1
                    max_streak = max(max_streak, counter)
                else:
                    counter = 1

        return max_streak




