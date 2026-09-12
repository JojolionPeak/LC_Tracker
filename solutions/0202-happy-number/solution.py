class Solution:
    def isHappy(self, n: int) -> bool:
        walk, num = set(), n
        while num != 1:
            number = str(num)
            new = [int(x)**2 for x in number]
            num = sum(new)
            if num not in walk:
                walk.add(num)
            else: return False
        return True
