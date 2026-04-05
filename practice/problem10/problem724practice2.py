# Incorrect but using it to test output

nums = [1,7,3,6,5,6]

total_sum= sum(nums)
left_sum=0
right_sum=total_sum-left_sum
for i in range(len(nums)):
    if left_sum == right_sum:
        print (i)
    else:
        left_sum = sum(nums[:i])
        right_sum = total_sum-left_sum-nums[i]

print (-1)