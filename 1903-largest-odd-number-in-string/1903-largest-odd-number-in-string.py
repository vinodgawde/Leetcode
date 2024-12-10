class Solution:
    def largestOddNumber(self, num: str) -> str:
        for char in range(len(num)-1,-1,-1):
            if int(num[char])%2==1:
                return num[0:char+1]
                
        return "" 
