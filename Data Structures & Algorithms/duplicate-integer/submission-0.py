class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        is_duplicate = False
        nums_set = set(nums)
        if len(nums_set) < len(nums):
            return True
        return False