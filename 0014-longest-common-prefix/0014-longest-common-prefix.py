class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        s=min(strs,key=len)
        for index,v in enumerate(s):
            for ch in strs:
                if ch[index] != v:
                    return ch[:index]
        return s        
            