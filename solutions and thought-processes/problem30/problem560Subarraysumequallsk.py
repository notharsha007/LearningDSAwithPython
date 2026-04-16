class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_sums = {0:1}
        for num in nums:
            current_sum += num
            diff = current_sum -k
            count += prefix_sums.get(diff,0)
            prefix_sums[current_sum] = prefix_sums.get(current_sum,0) +1
        return count
    
''' My Thought Process And Experience

This problem required me to return the number of contiguos subarrays such that its sum equalls k
There is no way a person reading this problem for the first time says "Yeah i can solve this", or finding this question in interview for the first time solves this.
This problem requires deep understanding and i probably cant explain the problem here. i saw a ytvideo for the explanation, he explained it clearly, still many cant understand the solution
Right now i understand this solution completely but definitely woulf forget on how toapproach and solve it in the future.
link of that video:https://www.youtube.com/watch?v=fFVZt-6sgyo
'''