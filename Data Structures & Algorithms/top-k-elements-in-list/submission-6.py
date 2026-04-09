class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        freq_buckets = [[] for i in range(len(nums)+1)]
        
        for num, freq in count.items():
            freq_buckets[freq].append(num)
        res = []
        for nlist in freq_buckets[::-1]:
            for n in nlist:
                res.append(n)
                k -= 1
                if k == 0:
                    return res