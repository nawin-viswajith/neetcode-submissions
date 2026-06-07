class Solution:
    def reverseBits(self, n: int) -> int:
        num = f'{n:032b}'
        return (int(num[::-1], 2))
