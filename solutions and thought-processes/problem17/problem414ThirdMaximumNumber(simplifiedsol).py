class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sortedarray =  sorted(set(nums), reverse= True)
        if len(sortedarray) >= 3:
            return sortedarray[2]
        else:
            return max(sortedarray)
        

''' Just a simplified solution, no optimization involved'''