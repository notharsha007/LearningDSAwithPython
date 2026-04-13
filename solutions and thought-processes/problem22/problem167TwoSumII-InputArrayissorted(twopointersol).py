class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left<right :
            current_sum = numbers[left]+numbers[right]
            if current_sum == target:
                return (left+1, right+1)
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        

''' My Thought process And Experience

This solution utilizes the fact that it is a sorted array, so we can do two pointer approach
the current sum assignment id one so that the complexity gets reduced.
'''