def isnum(c_ascii):
    return 48 <= c_ascii <= 57

def islower(c_ascii):
    return 97 <= c_ascii <= 122

def isupper(c_ascii):
    return 65 <= c_ascii <= 90

def isalphanum(c):
    c_ascii = ord(c)
    return (isupper(c_ascii) 
                or islower(c_ascii) 
                or isnum(c_ascii))

def tolower(c):
    c_ascii = ord(c)
    if isnum(c_ascii) or islower(c_ascii):
        return c
    return chr(c_ascii + 32)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not isalphanum(s[l]):
                l += 1
            while r > l and not isalphanum(s[r]):
                r -= 1
            if l > r or tolower(s[l]) != tolower(s[r]):
                # print(s[l])
                # print(s[r])
                return False
            l, r = l + 1, r -1
        return True
            

        