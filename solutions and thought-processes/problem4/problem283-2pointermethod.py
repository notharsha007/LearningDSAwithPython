class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow= 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[slow], nums[i] = nums[i], nums[slow]
                slow += 1


''' My Thought Process And Experience

The problem required me to shift the 0's of the array behind the array and non zero values in the front without changing the order.
Before solving this problem, i learnt two pointers and quick swap. I struggled for some time and asked for guidance. It told me to think like: dont try to push the zeros to the end,
instead try to pull the non 0's to the front.

Time complexity:

O(n)

Space complexity:

O(1)

This is optimal.
 '''