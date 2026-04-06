class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indecies_dict = dict()
        for i, j in enumerate(nums):
            diff = target - j
            if diff in indecies_dict:
                return [indecies_dict[diff], i]
            indecies_dict[j] = i