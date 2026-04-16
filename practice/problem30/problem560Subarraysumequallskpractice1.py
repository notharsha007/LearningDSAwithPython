# Youtube solution works
nums = [1,2,3]
k = 3

count= 0
current_sum= 0
prefixsums = {0:1}

for num in nums:
    current_sum += num
    diff = current_sum - k
    count += prefixsums.get(diff,0)
    prefixsums[current_sum] = 1 + prefixsums.get(current_sum,0)
print(count)
