class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string = list(zip(sorted(s), sorted(t)))
        if len(string) != max(len(s), len(t)):
            return False
        for i in string:
            if i[0] != i[1]:
                return False
        return True