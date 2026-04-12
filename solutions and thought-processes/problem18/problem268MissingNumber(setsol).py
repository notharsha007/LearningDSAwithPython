class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=set(nums)
        for i in range(len(nums)+1):
            if i not in s:
                return i
        

''' This solution gives the best complexity 

Complexity
Type	Complexity
Time	O(n)
Space	O(n)
'''