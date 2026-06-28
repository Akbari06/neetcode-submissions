from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort to group duplicates together
        
        def backtrack(i, subset):
            # If we've reached the end of the list, add a copy of the subset to the results
            if i == len(nums):
                res.append(subset[::])
                return
            
            # Include nums[i] in the subset
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()  # Backtrack

            # Skip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # Exclude nums[i] from the subset and move to the next unique element
            backtrack(i + 1, subset)
        
        backtrack(0, [])
        return res

        
            
