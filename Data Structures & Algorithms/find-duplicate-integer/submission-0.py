class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = dict()
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
        val = max(counts.values())
        for key, value in counts.items():
            if val == value:
                return key
