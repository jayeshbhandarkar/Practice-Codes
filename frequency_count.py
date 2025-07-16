def countFrequency(arr):
    count = {} 

    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    for key, value in count.items():
        print(key, value)

arr1 = [10, 5, 10, 15, 10, 5]
arr2 = [2, 2, 3, 4, 4, 2]

countFrequency(arr1)
countFrequency(arr2)


"""
class Solution(object):
    def majorityElement(self, nums):
        count = 0
        elements = None

        for num in nums:
            if count == 0:
                elements = num
            if num == elements:
                count+=1
            else:
                count-=1
    
        return elements

obj = Solution()
nums = [3, 2, 3]
result = obj.majorityElement(nums)
print(result)
"""


"""
from collections import Counter
def countFrequency(arr):
    freq = Counter(arr)
    for key, value in freq.items():
        print(key, value)

arr1 = [10, 5, 10, 15, 10, 5]
arr2 = [2, 2, 3, 4, 4, 2]
countFrequency(arr1)
countFrequency(arr2)
"""
