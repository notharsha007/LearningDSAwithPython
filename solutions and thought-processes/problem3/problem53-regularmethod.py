class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum= nums[0]
        max_sum= nums[0]
        for i in nums[1:]:
            current_sum = max(i, current_sum+i)
            max_sum= max(max_sum,current_sum)
        return max_sum
    

''' My thought Process and Experience

This problem required me to return the maximum sum of subarrays where the numbers are contiguous(meaning they have to be near near each other).
While studying for the problem, chapgpt recommended the core statements needed to solve this problem so there want much of my input in this.
while solving the first attempt i used to initalize the variables like current_sum = 0 and max-sum = 0. Which wont work when the array is filled with negative numbers.
So this approach was taken and in the for loop we are slicing away the first element spcifically.

Time complexity:

O(n)

Space complexity:

O(1)

You only use two variables.
 '''