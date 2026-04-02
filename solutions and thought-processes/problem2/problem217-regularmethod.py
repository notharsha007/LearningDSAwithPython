class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for i in nums:
            if i in seen:
                return True
            else :
                seen.add(i)
        return False
    

''' My Thought Process And Experience

This problem required me to return true if there were any duplicates and false if there were any.
before appraoching the problem, i learnt about sets data type. Which only stores non duplicate values.

Complexity: O(n) only one for loop.the set() only consists of O(1).
 '''