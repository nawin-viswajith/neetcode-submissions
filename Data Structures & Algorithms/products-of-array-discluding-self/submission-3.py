# class Node:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next

# class LinkedList:
#     def __init__(self, values):
#         self.head = None
#         prev = None
#         for i in values:
#             node = Node(i)
#             if not self.head:
#                 self.head = node
#             else:
#                 prev.next = node
#             prev = node

#     def to_list(self):
#         values = []
#         current = self.head
#         while current:
#             values.append(current.value)
#             current = current.next
#         return values

# def product(nums):
#     LL = LinkedList(nums)
    
#     pref_prods = []
#     curr = LL.head
#     pref_prod = 1
#     while curr:
#         pref_prods.append(pref_prod)
#         pref_prod *= curr.value
#         curr = curr.next
    
#     suf_prod = 1
#     curr = LL.head
#     res = [0] * len(nums)
#     for i in range(len(nums) - 1, -1, -1):
#         res[i] = pref_prods[i] * suf_prod
#         suf_prod *= nums[i]
    
#     return res

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#             return product(nums)
import math, numpy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # result = []
        # for i in range(len(nums)):
        #     temp = nums.copy()
        #     temp.remove(nums[i])
        #     result.append(math.prod(temp))
        # return result
        result = []
        for i in range(len(nums)):
            x = nums[:i]+nums[i+1:]
            result.append(numpy.prod(x))
        return result
