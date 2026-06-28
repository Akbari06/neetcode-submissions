class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        # 1 2 4 6

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i] # 1 1 2 8
        
        postfix = 1

        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i] #   48 24 12 8
        
        return res