class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter = 0
        for num in nums:
            digits = len(str(num))
            if digits %2 == 0 :
                counter += 1
        return counter
    


''' My Thought Process And Experience

The problem wanted me to return the number of even digit numbers present in the array.
This required me to access each element of the array and convert thme to string so that we can find the number of digits using len().
and this lenght can be floored like this digits %2 ==0 so that when true, they posses even number of digits and they cna be added to the counter.
And finally after checking all the elements, we return the counter.

Time
O(n)

You scan the array once.

Space
O(1)

Only a counter variable is used.

(The temporary string doesn't count toward algorithmic space.)
'''