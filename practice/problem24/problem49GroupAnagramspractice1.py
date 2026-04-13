strs = ["eat","tea","tan","ate","nat","bat"]
group={}

for ch in strs:
    key = "".join(sorted(ch))
    if key not in group:
        group[key] = []
    group[key].append(ch)
print(list(group.values()))
    
