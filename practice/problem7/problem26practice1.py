# Attempt 1
nums = [0,0,1,1,1,2,2,3,3,4]

nums=set(nums)
k=len(nums)
print(k,nums)

# This failed because when assigning nums again, it reinitiates the variable nums which the problem doesnt wants.