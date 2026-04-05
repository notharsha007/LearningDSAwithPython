nums = [0,0,1,1,1,2,2,3,3,4]
seen={}
index=0
for i in range(len(nums)):
    if nums[i] not in seen:
        nums[index]= nums[i]
        seen[i] = nums[i]
        index += 1
    else:
        continue
k=len(nums)
print(k, nums)

# This also doesnt work because 1. in line 7 i am trying to insert key value pairs, which is something not needed and wont work for this solution 2. the else part is redundandt 3. 
# the len(nums) gives be the bloated value(along with the null values).