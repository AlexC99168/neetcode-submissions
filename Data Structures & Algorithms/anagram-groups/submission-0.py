class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        seen = dict()
        counter = 0
        
        for s in strs:
            t = tuple(self.strToList(s))
            if t in seen:
                res[seen[t]].append(s)
            else:
                res.append([s])
                seen[t] = counter
                counter += 1
        return res

    def strToList(self, s: str) -> List[str]:
        res = [0] * 26

        for sc in s:
            res[ord(sc)-ord('a')] += 1
        
        return res
