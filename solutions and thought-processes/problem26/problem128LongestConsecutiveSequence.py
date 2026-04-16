class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        for num in set_nums:
            if num-1 not in set_nums:
                current = num
                length = 0
                while current in set_nums:
                    current +=1
                    length +=1
                longest = max(longest, length)
        return longest
    

''' My Thought Process And Experience

This problem required me to return the longest sequence of numbers in a given array.
This took a lot of time to  solve, First i couldnt figure  out the logic of finding the consecutive numbers and my first attempt had many forloops and while loops.
I also couldnt figure out how to setup the while loop. I admit i tried but couldnt find the solution, so i saw the solution and finished it.Nothing to be proud of... just read and typed the code around
3 times.
'''