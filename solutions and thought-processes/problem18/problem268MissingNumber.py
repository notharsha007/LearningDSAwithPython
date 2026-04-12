class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i


''' My Thought Process And Experience

The problem required me to find the missing number in an array between 0 and n. n is the size of the array.
for this iterate through 0 to n+1 numbers so that n+1 is not considered but n is, we check each and every element in the array for missing number and we return that number

time complexity o(n)sq(which  is bad)
'''