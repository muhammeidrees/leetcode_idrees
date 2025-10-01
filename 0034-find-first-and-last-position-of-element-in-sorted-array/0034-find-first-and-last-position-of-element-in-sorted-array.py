class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s=[]
        for n in range(len(nums)):
            if nums[n] == target:
                s.append(n)
        if not s:
            return [-1,-1]
        return [s[0],s[-1]]
