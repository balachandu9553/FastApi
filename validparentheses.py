def valid_parentheses(s: str):
    stack = []
    hash_map = {'}':'{',']':'[',')':'('}
    for symbol in s:
        if stack and symbol in hash_map and hash_map[symbol] == stack[-1]:
            stack.pop()
        else:
            stack.append(symbol)
    if stack:
        return False
    return True

s = "{}{}]"
print(valid_parentheses(s))
