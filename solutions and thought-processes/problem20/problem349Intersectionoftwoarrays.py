class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        s1=set(nums1)
        s2=set(nums2)
        ans= list(s1&s2)
        return ans
        

''' My Thought Process and Experience

This problem required me to return the array with  common numbers present in two arrays,
first we convert the array to set form so that duplicates are removed, then we can perform set operations and get a result set, 
which can be converted back into list and returned.
'''