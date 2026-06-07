class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        for i in range(n+1):
            l.append(str(bin(i)).strip('0b').count('1'))
        return l