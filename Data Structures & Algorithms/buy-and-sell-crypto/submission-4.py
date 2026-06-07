# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         b = []
#         for i in range(len(prices)):
#             curr = prices[i]
#             best = curr
#             for j in range(i, len(prices)):
#                 if prices[j] > best:
#                     best = prices[j]
#                     b.append([curr, best])
#         if len(b) == 0:
#             return 0
#         x = [b[i][1] for i in range(len(b))]
#         y = [b[i][0] for i in range(len(b))]
#         return (max(x)-min(y))

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min = prices[0]
        for i in prices:
            print(i, min, res)
            if i < min:
                min = i
            res = max(res, i - min)
        return res
