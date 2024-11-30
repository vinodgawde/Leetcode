class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        temp = x
        if x<0:
            return False
        while temp!=0:
            ld=temp%10
            rev=rev*10+ld
            temp=temp//10
        if x != rev:
            return False
        else:
            return True
        