# Correctsolution received

s = "egg"
t = "add"
mapingst={}
mapingts={}
for c1,c2 in zip(s,t):
    if c1 in mapingst:
        if mapingst[c1] != c2:
            print(False)
    else:
        mapingst[c1] = c2
    if c2 in mapingts:
        if mapingts[c2] != c1:
            print(False)
    else:
        mapingts[c2] = c1
print(True)