class Solution:
    def hammingWeight(self, n: int) -> int:
        x = str(bin(n)).lstrip('0b')
        return x.count('1')
        