class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency={}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] =1
        ans= sorted(frequency, key=frequency.get, reverse=True)
        return ans[0:k]
    

''' My Thought Process And Experience

The problem required me to return k most frequent elementsof an array.
So we first caluclate the frequency of every number, and we get the sorted array by using the key filter expression as ans array
then we slice the ans array to return only k elements. There are better codes than this.

Time Complexity
O(n log n)

Why?

Building dictionary → O(n)
Sorting → O(n log n)
Space Complexity
O(n)

For the frequency dictionary.
'''