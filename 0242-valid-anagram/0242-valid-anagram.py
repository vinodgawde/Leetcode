class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash={}
        if len(s) != len(t):  
            return False
            
        for char in s:
            s_hash[char]=s_hash.get(char,0)+1

        for char in t:
            if s_hash.get(char,0) == 0:
                return False
            s_hash[char]-=1
            
        return True