class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dfs(i,hold):
            if i <0 :
                return -inf if hold else 0
            if hold:
                return max(dfs(i-1,True),dfs(i-1,False) - prices[i])
            return max(dfs(i-1,False),dfs(i-1,True) + prices[i])
        return dfs(n-1,False)
        