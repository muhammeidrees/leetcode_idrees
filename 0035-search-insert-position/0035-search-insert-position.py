class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        target_index = 0
        for index,num in enumerate(nums):
            if num == target:
                target_index = index
            elif num < target:
                target_index = index + 1
            else:
                break
        return target_index