class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        li = []

        for i in range(len(s)-1,-1,-1):
            li.append(s[i])

        li = ''.join(li)

        if s == li:
            return True

        return False

        
