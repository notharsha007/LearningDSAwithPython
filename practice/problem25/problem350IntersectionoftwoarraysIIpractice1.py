# Nice, got the ans

nums1 = [1,2,2,1]
nums2 = [2,2]

d1={}
result=[]

for num in nums1:
    if num in d1:
        d1[num] += 1
    else:
        d1[num] = 1
for num in nums2:
    if num in d1 and d1[num] > 0:
        result.append(num)
        d1[num] -=1
print(result)