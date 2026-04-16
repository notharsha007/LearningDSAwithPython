nums = [100,4,200,1,3,2]
set_nums = set(nums)
longest = 0
for num in set_nums:
    if num-1 not in set_nums:
        current = num
        length = 1
        while current in set_nums:
            current +=1
            length += 1
        longest = max(longest, length)
print(longest)

