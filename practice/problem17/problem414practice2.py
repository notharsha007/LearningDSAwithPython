# incorrect solution

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique = set(nums)
        sortedarray =  sorted(unique, reverse= True)
        if sortedarray[2] == None:
            return sortedarray[1]
        elif sortedarray[1]== None:
            return sortedarray[0]
        else:
            return sortedarray[2]