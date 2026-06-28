class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            newList = []
            for y in range(len(nums)):
                if nums[x] + nums[y] == target and x != y:
                    newList.append(x)
                    newList.append(y)
                    return newList

        