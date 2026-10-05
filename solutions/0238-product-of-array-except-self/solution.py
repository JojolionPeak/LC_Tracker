class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer, right = [1], 1

        for i in range(1, len(nums)):
            answer.append(answer[-1] * nums[i-1])

        for i in range(len(nums)-1, -1, -1):
            answer[i] *= right
            right *= nums[i]
            
        return answer
