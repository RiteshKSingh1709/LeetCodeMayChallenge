class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        from collections import Counter
        c = Counter(S)
        result = 0
        for i in J:
            result += c[i] if c.get(i) is not None else 0
        print(result)
        return result