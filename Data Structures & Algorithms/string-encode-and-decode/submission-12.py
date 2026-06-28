class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""

        for i in strs:
            res += str(len(i)) + "#" + i

        return res # 5#hello5#world

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res





