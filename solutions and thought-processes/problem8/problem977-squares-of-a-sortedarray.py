class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square= [x*x for x in nums]
        square.sort()
        return square
    

    
''' My Thought Process And Experience

Just knew how to do list comprehension, and had to sort it and return

Time Complexity

Squaring elements:

O(n)

Sorting:

O(n log n)

Total:

O(n log n)
Space Complexity

You created a new list:

square

So space complexity:

O(n)
'''