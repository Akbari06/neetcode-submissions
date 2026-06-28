class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        sorted_nums = sorted(count.keys(), key=lambda x: count[x], reverse=True)
        
        # Return the top k frequent numbers
        return sorted_nums[:k]