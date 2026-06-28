class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        dic = defaultdict(int)
        temp = []
        res = []

        for i in nums:
            dic[i] += 1
        
        for num, count in dic.items():
            temp.append([num,count])

        temp = sorted(temp, key = lambda x : -x[1])

        return [num for num, count in temp[:k]]

        