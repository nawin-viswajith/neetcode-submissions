class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        set_nums = sorted(list(set(nums)))
        ele_count = []
        for num in set_nums:
            ele_count.append(nums.count(num))
        res = sorted(zip(ele_count, set_nums))[-k:]
        res_list = [i[1] for i in res]
        return res_list