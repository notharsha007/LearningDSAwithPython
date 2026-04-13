class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)    
    

''' This is a one line solution which uses  the collections.counter to get the frequency of chars in the string

Complexity
Type	Complexity
Time	O(n)
Space	O(n)
'''