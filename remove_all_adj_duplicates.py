def removeDuplicates(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()

        else:
            stack.append(char)

    return "".join(stack)
        
s = input()
result = removeDuplicates(s)
print(result)
