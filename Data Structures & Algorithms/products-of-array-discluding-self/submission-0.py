class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for n in nums]
        for i in range(len(nums)):
            output[:i] = map(lambda x: x*nums[i], output[:i])
            output[i+1:] = map(lambda x: x*nums[i], output[i+1:])
        return output