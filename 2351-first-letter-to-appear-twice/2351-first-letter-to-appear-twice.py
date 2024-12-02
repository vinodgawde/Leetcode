class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hashmap={}
        for char in s:
            if char in hashmap:
                hashmap[char]+=1
                if hashmap[char]==2:
                    return char
            else:
                hashmap[char]=1
        