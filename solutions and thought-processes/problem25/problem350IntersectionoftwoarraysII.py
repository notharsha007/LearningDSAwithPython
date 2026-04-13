class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        frequency= {}
        result=[]
        for num in nums1:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        for num in nums2:
            if num in frequency and frequency[num] > 0 :
                result.append(num)
                frequency[num] -= 1
        return result
        

'''My Thought Process And Experience

This problem required me to return an array conisting of common elements between two arrays, but this time, duplicates are allowed.
This was hard, and struggled for some time. Eventually with helpof ai(without revealing the answer), i managed to think about initially storing the frequency of 1st array
and then compare the second array to get common elements and append it to the result while we are reducing the frequency so that they dont get added continuously.
Time Complexity
O(n + m)
First loop → O(n)
Second loop → O(m)
Dictionary lookup → O(1)

👉 This is optimal

Space Complexity
O(n)

For the frequency dictionary.
'''