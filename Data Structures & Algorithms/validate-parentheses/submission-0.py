class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # "([])"
        map_ = {"}" : "{", ")" : "(", "]" : "["}
       # [ ( , [ ]
        for c in s:
            if c not in map_:
                stack.append(c) 
                continue
         
            else:
                if not stack or stack[-1] != map_[c]:
                    return False
                stack.pop()

        return not stack

