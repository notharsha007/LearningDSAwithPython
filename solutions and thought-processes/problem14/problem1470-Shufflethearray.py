class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[]
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans
        

'''My Thoughts And Experience

This problem required me to shuffle the array such that the subsequent elements in the second half of the array is merged along with the subsequent elements of the first half.
First i tried to iterate over range(len(n)), but that wont work because i+n would exceed the loop limit. So we can iterate till n and add the elements int he desired order.
'''