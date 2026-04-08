class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        res = list(count.items())
        res.sort(key = lambda x: x[1], reverse=True)
        return [item[0] for item in res[:k]]