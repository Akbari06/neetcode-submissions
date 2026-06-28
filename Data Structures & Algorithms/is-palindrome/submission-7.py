class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for i in s:
            if i.isalnum():
                newStr += i.lower()

        if newStr == newStr[::-1]:
            return True 
        else:
            return False