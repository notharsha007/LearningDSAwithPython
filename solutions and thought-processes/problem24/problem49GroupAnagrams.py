class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for ch in strs:
            key = "".join(sorted(ch))
            if key not in group:
                group[key] = []
            group[key].append(ch)
        return list(group.values())
    
''' My Thoughts And Experience

This problem required me to return a grouped lists of anagrams of strings in a list.
This took a lot of time to solve. after some thinking, i could get about half the logic right but was always lacking some of it.
We first create a dictionary with key: value pairs as a standard sorted word string as a key and the value assigned to that particualr key as string that we iterate.
since array connot be a dict value we have to covert it to string and the value could be an array, so that is what is being done here.

Time Complexity
O(n * k log k)
n = number of strings
k = length of each string
sorting each string → k log k
Space Complexity
O(n * k)
storing grouped strings
'''