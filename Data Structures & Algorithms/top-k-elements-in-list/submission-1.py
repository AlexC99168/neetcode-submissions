class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = dict()
        res = []

        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        n = len(nums)
        buckets = [[] for _ in range(n+1)]

        for key in seen:
            buckets[seen[key]].append(key)
        
        for i in range(n, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res