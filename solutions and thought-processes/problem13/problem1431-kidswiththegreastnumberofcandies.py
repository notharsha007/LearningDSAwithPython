class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy= max(candies)
        ans=[]
        for candy in candies:
            total_candy = candy + extraCandies
            if total_candy >= max_candy:
                ans.append(True)
            else:
                ans.append(False)
        return ans
    
''' My thought Process And Experience

The problem required me to return the array filled with boolean values of wheather the kid is gonna have the greatest amount of candy when the extra candies are given to them.
So i calculated the max candies a kid has, then checked for every kid wheter they they willhave the max or not, store the result value in the ans array.

Time
O(n)
max() → O(n)
loop → O(n)

Total still O(n).

Space
O(n)

Because of the result list.
'''