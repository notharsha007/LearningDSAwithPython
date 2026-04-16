class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapingst={}
        mapingts={}
        for ch1,ch2 in zip(s,t):
            if ch1 in mapingst:
                if mapingst[ch1] != ch2:
                    return False
            else:
                mapingst[ch1] = ch2
            if ch2 in mapingts:
                if mapingts[ch2] != ch1:
                    return False
            else:
                mapingts[ch2]= ch1
        return True
    
''' My Thought Process And Experience

This problem required me to return true or false basedon whether the strings are isomorphic or not.
I didnt know the logic to access the characters of bot  the strings at the same time also was notconfident in using if loop inside another if loop. So i gave up on solving this
Then upon seeing the solution, i saw we have to use zip() to access them both at the same time. We need to use two mappings one for checking if ch1 is mapped to ch2 or not. And
the second one is for checking if ch2 is mapped to ch1 or not.

Complexity
Time: O(n)
Space: O(n)
'''