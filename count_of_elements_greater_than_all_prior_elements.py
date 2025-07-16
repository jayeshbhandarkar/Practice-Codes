def countGreaterElements(arr):
    # Initialize the count and the variable to track the maximum seen so far
    count = 0
    max_so_far = float('-inf')  # Start with negative infinity
    
    # Iterate through the array
    for num in arr:
        # If the current number is greater than the maximum seen so far
        if num > max_so_far:
            count += 1
            max_so_far = num  # Update the maximum seen so far
    
    return count

arr = [7, 4, 8, 2, 9]
print(countGreaterElements(arr))


"""
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max = float('-inf')

        for candy in candies:
            if candy > max:
                max = candy

        result = []

        for candy in candies:
            if candy + extraCandies >= max:
                result.append(True)
            else:
                result.append(False)

        return result
    
ob = Solution()
candies = [2,3,5,1,3]
extraCandies = 3
ans = ob.kidsWithCandies(candies, extraCandies)
print(ans)
"""
