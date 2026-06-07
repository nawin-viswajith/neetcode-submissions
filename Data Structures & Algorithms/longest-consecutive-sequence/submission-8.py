class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort() 
        seq, max_seq = 1, 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                seq += 1
            elif nums[i] != nums[i - 1]:
                seq = 1
            max_seq = max(max_seq, seq)

        return max_seq