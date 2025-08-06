class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inex=[]
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j] == target:
                    inex.append(i)
                    inex.append(j)
        return inex