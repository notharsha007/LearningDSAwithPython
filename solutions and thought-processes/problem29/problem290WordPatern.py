class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()
        chtoword =  {}
        wordtoch = {}
        if len(pattern) != len(word):
            return False
        for a,b in zip(pattern,word):
            if a in chtoword and chtoword[a] !=b :
                return False
            else:
                chtoword[a] = b
            if b in wordtoch and wordtoch[b] != a:
                return False
            else:
                wordtoch[b] = a
        return True
    
''' My Thought Process And Experience

This problem required me to return true or false if the words of "s" match the characters of "pattern".
This was easy to solve because the last problem was extremely similar to this.
In the previous problem we used to compare ch to ch, but here we compare a ch to a word. Also we check for lengths between the characters and words before we goto mapping and checking process.
'''