class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += '#'
            res += s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        counter = ''

        while i < len(s):
            if s[i] == '#':
                l = int(counter)
                counter = ''
                res.append(s[i+1:i+l+1])
                i += l + 1
                continue
            counter += s[i]
            i += 1
        return res