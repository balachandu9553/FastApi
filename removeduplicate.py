def removeAllAdjacentDuplicates(s):
    stack = []


    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
            print(stack)
        else:
            stack.append(i)
    return "".join(stack)


s = "abbaca"
result = removeAllAdjacentDuplicates(s)
print(result)