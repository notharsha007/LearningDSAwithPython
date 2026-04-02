class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)) :
                if nums[i] + nums[j] == target :
                    return [i,j]
                

''' My Thought Process and experience:
I understood the problem requires me to give the indices of two numbers in an array whose sum is equivalent to that of the target given.
This is my first method of solving it which is nothing but the brute force.
First, I have to fix a number and add it with the other numbers present in the array.
To fix that number the first for-loop array and the second for-loop array for the other numbers.
The solution is simple enough, but i was stuck on the second for-loop, my idea was right , but i could'nt recollect the syntax for setting the starting point and the end point in range.
 '''