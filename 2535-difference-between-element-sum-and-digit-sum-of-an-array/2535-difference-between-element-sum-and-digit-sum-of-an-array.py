class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        el_sum=sum([num for num in nums])
        d="".join([str(n) for n in nums])
        d_sum=sum([int(el) for el in d])
        return el_sum-d_sum