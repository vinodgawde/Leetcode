class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        is_negative = False
        if x<0:
            is_negative = True
            x *= -1
        while x>0:
            ld=x%10
            rev=(rev*10)+ld
            x=x//10
        if rev > 2** 31-1:
            return 0
        return rev * -1 if is_negative else rev
        