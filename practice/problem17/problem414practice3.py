# Incorrect but closer to answer

nums = [1,2]
unique = set(nums)
sortedarray =  sorted(unique, reverse= True)
length = len(sortedarray)
if length >= 3:
    print (sortedarray[2])
elif length == 2:
    print (sortedarray[1])
else:
    print (sortedarray[0])

print(length)