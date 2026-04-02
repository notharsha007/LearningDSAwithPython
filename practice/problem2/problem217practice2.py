# Program to check for any duplicate

arr=[1,4,7,1]
seen=set()
for i in arr:
    if i in seen :
        print("There is a duplicate")
    else :
        seen.add(i)