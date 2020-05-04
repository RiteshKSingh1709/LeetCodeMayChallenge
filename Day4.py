class Solution:
    def findComplement(self, num: int) -> int:
        result = ''
        for i in bin(num)[:2]:
            result += '1' if i == '0' else '0' 
        return int(result,2)
