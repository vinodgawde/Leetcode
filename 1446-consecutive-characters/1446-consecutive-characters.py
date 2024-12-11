class Solution:
    def maxPower(self, s: str) -> int:
        count=1
        maxval=1
        for i in range(1,len(s)):
            if s[i-1]==s[i]:
                count+=1
            else:
                count=1
            if maxval<count:
                maxval=count
        return maxval
