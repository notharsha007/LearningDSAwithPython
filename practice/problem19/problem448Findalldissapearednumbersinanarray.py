nums = [4,3,2,7,8,2,3,1]
ans=[]

s= set(nums)
for i in range(1,len(nums)+1):
    if i not in s:
        ans.append(i)

print(ans)