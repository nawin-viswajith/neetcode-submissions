class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''.join(i.lower() for i in s if i.isalnum())
        s = a[::-1]
        for i in range(len(a)):
            print(a[i], s[i])
            if a[i] != s[i]:
                return False
        return True
        