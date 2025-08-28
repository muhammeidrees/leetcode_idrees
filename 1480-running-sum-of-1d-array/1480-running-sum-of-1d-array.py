class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new=[]
        new.append(nums[0])
        for i in range(1,len(nums)):
            new.append(nums[i]+new[i-1])
        return new