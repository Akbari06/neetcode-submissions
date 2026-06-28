class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i, val in enumerate(s):
            lastIndex[val] = i
        
        res = []
        size, end = 0, 0
        for i, val in enumerate(s):
            size += 1
            end = max(end, lastIndex[val])

            if i == end:
                res.append(size)
                size = 0
        
        return res