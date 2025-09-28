class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(int(n/2)):
            temp=nums[n-1-i]
            nums[n-1-1]=nums[i]
            nums[i]=temp
        return nums