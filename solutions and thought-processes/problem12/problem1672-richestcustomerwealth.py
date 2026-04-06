class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth=0
        wealth=0
        for account in accounts:
            wealth = sum(account)
            max_wealth = max(max_wealth, wealth)
        return max_wealth
    

''' My Thought Process And Experience

This problem wants me to reaturn the customer with the highest wealth. We can iterate the every customers every bank using that for loop, and keep track of the wealth of every customer
and find out the maxwealth among all customers

Time Complexity
O(m × n)

Where:

m = number of customers
n = number of banks

Because sum(account) scans each row.

Space Complexity
O(1)

Only two variables are used.
'''