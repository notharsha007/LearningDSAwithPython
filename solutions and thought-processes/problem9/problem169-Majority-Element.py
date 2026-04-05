class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash={}
        for i in range(len(nums)):
            if nums[i] in hash:
                hash[nums[i]] += 1
            else:
                hash[nums[i]] = 1
        return max(hash, key=hash.get)
        

''' My Thoughts And Experience

By reading the question it can be understood that we need to play with frequencey,so hashmaps. We traverse through the array and add the element and its frequency.
The hard part trying to understand: how to return the key whose frequency is the highest? I tried but couldnt figure out, then discovered we have to accomodate a max statement with the
syntax shown above.

Complexity

Time Complexity:

O(n)

Space Complexity:

O(n)
'''