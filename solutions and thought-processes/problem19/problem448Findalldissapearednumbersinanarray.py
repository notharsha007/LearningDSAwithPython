class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans=[]
        s=set(nums)
        for i in range(1,len(nums)+1):
            if i not in s:
                ans.append(i)
        return ans
        
''' My Thoughts and Experience

This problems requires me to return an array of missing elements from the range 1 to n from the given array.
This problem is almost exact to that of the previous problem. Used the same approach to finding and appending the missing elements of the array.
'''