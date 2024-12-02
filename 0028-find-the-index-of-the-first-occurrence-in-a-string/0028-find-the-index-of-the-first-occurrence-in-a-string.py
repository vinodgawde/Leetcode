class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m=len(haystack)
        n=len(needle)
        for i in range(m-n+1):
            for j in range(n):
                if haystack[i+j]!=needle[j]:
                    break
                if j == n-1:
                    return i 
        return -1

        