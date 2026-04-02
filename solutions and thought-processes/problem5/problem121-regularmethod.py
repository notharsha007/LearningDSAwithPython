class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price= prices[0]
        max_profit= 0
        for i in prices:
            min_price= min(min_price,i)
            max_profit= max(max_profit, i-min_price)
        return max_profit
    

''' My Thoughts And Experience

The problem required me to give the maximum profit one can make in the given situation.
For this problem i initially tried to solve it by finding the indices and other useless methods. Ofcourse with some guidance, having to know i have to continuosly kepp scanning for
the minimum prize possible and maximum profit possible. The min-max approach came in handy.
'''