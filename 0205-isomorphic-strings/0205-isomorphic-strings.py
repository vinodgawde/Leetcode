class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap ={}
        for char in range(len(s)):
            if s[char] not in hashmap:
                if t[char] in hashmap.values():
                    return False
                hashmap[s[char]]=t[char]
            else:
                if hashmap[s[char]]!=t[char]:
                    return False
        return True