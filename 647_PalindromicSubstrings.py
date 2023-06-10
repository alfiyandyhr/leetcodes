class Solution:
    def countSubstrings(s: str) -> int:
        # O(n^2) time
        res = 0
        for i in range(len(s)):
            # Odd case
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            # Even case
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res

    def countSubstrings2(s: str) -> int:
        # O(n^2*n) time
        def isPalindrome(x):
            if len(x) == 1:
                return True
            else:
                l, r = 0, len(x)-1
                while l < r:
                    if x[l] != x[r]:
                        return False
                    l += 1
                    r -= 1
                return True
        
        res = 0
        for i in range(len(s)):
            for j in range(len(s)):
                subString = s[i:j+1]
                if isPalindrome(subString) and subString != '':
                    res += 1
        
        return res

s = 'abc'
# s = 'aaa'

print(Solution.countSubstrings(s))
print(Solution.countSubstrings2(s))