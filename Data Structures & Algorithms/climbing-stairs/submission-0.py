class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        x, y = 2, 3

        for i in range(4, n+1):
            temp = x + y
            x = y
            y = temp
            print(x, y, temp)
        return y