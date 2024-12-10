class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxval=-1
        for i in range(2,len(num)):
            if (num[i]==num[i-1]):
                if num[i-1]==num[i-2]:
                    if maxval < int(num[i]):
                        maxval=int(num[i])
        if maxval == -1:
            return ""
        return str(maxval) * 3
            