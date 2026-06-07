class Solution:
    def isValid(self, s: str) -> bool:
        dict_p = {']':'[', ')':'(', '}':'{'}
        l = []
        for i in s:
            if i not in dict_p:
                print('1',i)
                l.append(i)
                continue
            if not l or l[-1]!=dict_p[i]:
                print(l, dict_p[i])
                return False
            print(not l)
            l.pop()
        return not l