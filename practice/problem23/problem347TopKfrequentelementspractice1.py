nums = [1,1,1,2,2,3]
k = 2

freq= {}
for i in range(len(nums)):
    if nums[i] in freq:
        freq[nums[i]] += 1
    else:
        freq[nums[i]] = 1
ans = sorted(freq, key=freq.get, reverse=True)
print(ans[0:k])