class Solution:
    def reverseVowels(self, s: str) -> str:
        v=["A","E","I","O","U","a","e","i","o","u"]
        new=[ch for ch in s if ch in v]
        sl=list(s)
        for i in range(len(s)):
            if s[i] in v:
                sl[i]=new.pop()
        return "".join(sl)
        