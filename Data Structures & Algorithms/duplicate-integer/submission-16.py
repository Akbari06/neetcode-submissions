class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            counter = 0
            for x in nums:
                if x==i:
                    counter += 1
                if counter > 1:
                    return True
                    break
        return False