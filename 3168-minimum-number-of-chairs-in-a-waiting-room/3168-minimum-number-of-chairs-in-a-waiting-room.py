class Solution:
    def minimumChairs(self, s: str) -> int:
        minimum_chair=0
        ava_chair=0
        for i in range(len(s)):
            if s[i]=='E':
                if ava_chair == 0:
                    minimum_chair+=1
                else:
                    ava_chair-=1
            else:
                if s[i]=='L':
                    ava_chair+=1
        
        return minimum_chair
        