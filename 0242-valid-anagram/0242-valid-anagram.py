class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash={}
        t_hash={}
        if len(s) != len(t):  
            return False
            
        for char in s:
            if char in s_hash:
                s_hash[char]+=1
            else:
                s_hash[char]=1
        for char in t:
            if char in t_hash:
                t_hash[char]+=1
            else:
                t_hash[char]=1  
        if s_hash == t_hash:
            return True
        return False  