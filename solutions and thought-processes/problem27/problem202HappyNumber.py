class Solution:
    def isHappy(self, n: int) -> bool:
        seen= set()
        while n!= 1:
            if n in seen :
                return False
            seen.add(n)
            total = 0
            while n>0:
                digit = n%10
                total += digit*digit
                n = n//10
            n = total
        return True


''' My Thought Process And Experience

This problem required me to return True or False if the given number is happy number or not.
This problem felt hard for me because i did not know the logic for digit extraction and was struggling to move on with the problem iniitally.
So what we are doing is we are maintaining set variable to store already calulated digits, so that when they are triggered again, we can stop the loop and return false,
And we are iterating using while loop till we get 1 as value of n.

Time: O(log n) per iteration
Space: O(log n) (set storage)
'''