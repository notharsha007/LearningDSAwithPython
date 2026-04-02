class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        for i in range(len(nums)):
            needed= target - nums[i]
            if needed in seen :
                return [i,seen[needed]]
            else :
                seen[nums[i]] = i



''' My Thought Process And Experience:

This method of solving requires hashmapping and solves this problem with O(n) complexity(the brute force appraoch required O(n)square which increases computation exponentially when the sample space grows).
We fix one number using for loop and calulate the required number needed to be added to make it up to the target. And then we chaeck if the number already exists on the dictionary(Which has the number as key and index of that number as value)
if it exists on dictionary, we return the i and the index of the nedded number, if not on dictionary, we store the value of i in seen dictionary.
 '''
