class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans=[]
        for sublist in accounts:
            sum=0
            for i in sublist:
                sum+=i
            ans.append(sum)
        return max(ans)