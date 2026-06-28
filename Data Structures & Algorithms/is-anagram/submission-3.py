class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = []
        t_list = []

        for x in s:
            s_list.append(x)
        for y in t:
            t_list.append(y)

        if sorted(s_list) == sorted(t_list):
            return True

        else:
            return False
            