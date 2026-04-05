class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen=set()
        index=0
        for i in range(len(nums)):
            if nums[i] not in seen:
                nums[index]= nums[i]
                seen.add(nums[i])
                index += 1
        k=len(seen)
        return k
    
''' My Thought Process And Experience

Understanding the question can be tricky, but once we understand how leetcode scans for values in backend, it is easy.
I Traveresd throught the list and compared each element whether they are in the set or not to modify the nums list. The list itself would be bloated in places of duplicates, but that wouldnt be an issue
then the count of the non duplicates were also asked we can either do len() or count() methods.
'''