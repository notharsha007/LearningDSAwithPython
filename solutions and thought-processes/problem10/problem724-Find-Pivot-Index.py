class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum= sum(nums)
        left_sum=0
        for i in range(len(nums)):
            right_sum=total_sum-left_sum-nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1
    
''' My Thought Process And Experience

This problem took me a while. The problem wanted me to find the pivot point in a list where the elements from that list left or right from a point must be having the same sum.
I couldnt figure out how to start with both the left and right sums at 0, because they must be checked for equallity in following lines.
Then i saw the method of using totalsum to keep track of the right sum. Since rightsum needs tobe excluded off the index element,they are moved inside the loop.
And then updating the leftsum and rightsum until they are equall, if not we return -1.
'''