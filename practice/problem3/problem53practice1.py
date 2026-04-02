''' 
Kadane’s Algorithm Idea

While scanning the array we track two things:

1️⃣ Current running sum
current_sum

Sum of the subarray we are currently building.

2️⃣ Best sum seen so far
max_sum

The best subarray sum we've found.

Step-by-Step Thinking

For each number:

num

We decide:

Should I continue the current subarray?
OR
Start a new subarray here?

Mathematically this becomes:

current_sum = max(num, current_sum + num)

Meaning:

Either start fresh with num
OR extend previous subarray

Then update best answer:

max_sum = max(max_sum, current_sum)
Small Example

Array:

[4,-1,2,1]

Step by step:

current_sum = 4
max_sum = 4

Next:

current_sum = max(-1, 4 + (-1)) = 3
max_sum = 4

Next:

current_sum = max(2, 3 + 2) = 5
max_sum = 5

Next:

current_sum = max(1, 5 + 1) = 6
max_sum = 6

Final answer:

6
'''