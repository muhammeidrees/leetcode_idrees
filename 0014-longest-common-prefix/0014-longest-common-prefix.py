class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest=min(strs,key=len)
        for index,ch in enumerate(shortest):
            for string in strs:
                if string[index]!=ch:
                    return shortest[:index]
        return shortest
