# practice 

nums = [12,345,2,6,7896]
counter = 0
for num in nums:
    digits = len(str(num))
    if digits %2 == 0 :
        counter += 1

print(counter)