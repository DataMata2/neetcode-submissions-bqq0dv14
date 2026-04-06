class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        indecies_dict = dict()
        for k in range(len(nums)):
            if nums[k] in indecies_dict:
                indecies_dict[nums[k]].append(k)
            else:
                indecies_dict[nums[k]] = [k]  
        nums.sort()
        while i != j:
            attempt = nums[i] + nums[j]
            if  attempt == target:
                answer = [indecies_dict[nums[i]].pop(), indecies_dict[nums[j]].pop()]
                answer.sort()
                return answer
            if attempt < target:
                i += 1
            else:
                j -= 1