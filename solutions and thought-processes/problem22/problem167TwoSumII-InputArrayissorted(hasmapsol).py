class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(numbers)):
            needed= target - numbers[i]
            if needed in seen:
                return [seen[needed] +1 , i+1]
            else:
                seen[numbers[i]] = i

'''My Thought Process And Experience

The problem required me to return the indices+1 of the SORTED array whose sum is  target.
I think this is the easy approach, because we just add+1 to the two sum question in the answer, but
we have to implement two pointer concept to this question since it is orted array, nonetheless this is a correct solution

Time Complexity
O(n)
Single loop
Dictionary lookup is O(1)
Space Complexity
O(n)

Because of the seen dictionary.
'''