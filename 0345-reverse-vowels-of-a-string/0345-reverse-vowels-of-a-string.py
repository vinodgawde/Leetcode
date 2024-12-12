class Solution:
    def reverseVowels(self, s: str) -> str:
        left,right=0,len(s)-1
        s = list(s)
        vowels = set('aeiouAEIOU')
        while left<right:
            while left<right and not s[left] in vowels:
                left+=1
            while left<right and not s[right] in vowels:
                right-=1
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1

        return ''.join(s)
        