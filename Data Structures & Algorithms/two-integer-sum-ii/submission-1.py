class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = []
        for i in numbers:
            if (target-i in numbers and target-i != i):
                    l.append(numbers.index(target-i)+1)
        return list(set(l))