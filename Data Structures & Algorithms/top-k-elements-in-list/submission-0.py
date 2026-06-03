class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = dict()
        res = []

        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        highest = len(nums)
        invert = dict()

        for key in seen:
            if seen[key] in invert:
                invert[seen[key]].append(key)
            else:
                invert[seen[key]] = [key]
        
        for i in range(highest, 0, -1):
            if i in invert:
                for num in invert[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
        return res