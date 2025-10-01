class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res="".join(str(num) for num in digits)
        res=int(res)
        res+=1
        res=str(res)
        return [int(num) for num in res]