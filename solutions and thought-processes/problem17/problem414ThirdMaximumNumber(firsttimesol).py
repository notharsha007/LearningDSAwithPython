class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique = set(nums)
        sortedarray =  sorted(unique, reverse= True)
        length = len(sortedarray)
        if length >= 3:
            return sortedarray[2]
        else:
            return max(sortedarray)
        

''' My Thought Process And Experience

This problem requried me to return the 3rd maximum number in an array, sounds easy, but the edge cases take some time to solve.
first we remove the duplicates and sort the array in reverse order, then we check the size of the sorted array so that if it is 3 or abovem we can  return the index2 element and if not 
we just return the max value of the array.

Time Complexity

O(n log n)

because sorting dominates.

Space Complexity

O(n)

because of the set and sorted list.

This is perfectly acceptable for most cases.
'''