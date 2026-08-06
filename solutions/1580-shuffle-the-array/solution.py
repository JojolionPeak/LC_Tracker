class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        out = []
        for i in range(n):
            cur, jump = nums[i], nums[i+n]
            out.append(cur)
            out.append(jump)
        return out
