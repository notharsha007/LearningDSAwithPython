class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        for ch in s:
            if ch in d1:
                d1[ch] += 1
            else:
                d1[ch] = 1
        for ch in t:
            if ch in d2:
                d2[ch] += 1
            else:
                d2[ch] = 1
        if d1 == d2:
            return True
        else:
            return False
        

''' My Thought Process And Experience

The problem required me to check if the string is an anagram of one another and return true or false.
i think this is a slow approach, since we are using 2 for loops and if else checks.might have to ask ai for shortcut methods to improve complexity

Time Complexity
O(n + m)
Loop through s → O(n)
Loop through t → O(m)
Compare dictionaries → O(1) average (bounded keys)
Space Complexity
O(n)

Because dictionaries store character counts.
'''