# Correct solution but doesnt check the length of patterns and words
pattern = "abba"
s = "dog cat cat dog"
word = s.split()

chtoword = {}
wordtoch = {}

for a,b in zip(pattern,word):
    if a in chtoword and chtoword[a] != b :
        print (False)
    else:
        chtoword[a] = b
    if b in wordtoch and wordtoch[b] != a:
        print (False)
    else:
        wordtoch[b] = a
print(True)