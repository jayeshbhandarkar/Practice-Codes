def twoSum(numbers, target):
    left, right = 0 , len(numbers)-1

    while left < right:
        if numbers[right] + numbers[left] == target:
            return [left+1, right+1]

        elif numbers[right] + numbers[left] > target:
            right -= 1

        else:
            left += 1

    return [-1, -1]

t = int(input())
for _ in range(t):
    numbers = list(map(int, input().strip('[]').split(',')))
    target = int(input())
    result = twoSum(numbers, target)
    print(result) 
