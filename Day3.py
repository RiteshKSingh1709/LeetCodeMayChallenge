class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        p1 = Counter(ransomNote)
        p2 = Counter(magazine)
        for k,v in p1.items():
            if p2[k] < v:
                return False
        return True
