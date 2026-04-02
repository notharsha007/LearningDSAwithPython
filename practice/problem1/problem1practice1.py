# program to count the fequency of numbers in the array

arrs= [5,78,34,5,34,34,89,0,3]
freq= {}
for arr in arrs:
    if arr in freq:
        freq[arr] += 1
    else :
        freq[arr] = 1
        
print(freq)
