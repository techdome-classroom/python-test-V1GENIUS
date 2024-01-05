def Solution(s):
    stack = []
    for ch in s:
        if ch in ('(', '{', '['):
            stack.append(ch)
        else:
            if stack and ((stack[-1] == '(' and ch == ')') or
                        (stack[-1] == '{' and ch == '}') or
                        (stack[-1] == '[' and ch == ']')):
                stack.pop()
            else:
                return False
    return not stack

expr = "(]"

# Function call
if Solution(expr):
    print("true")
else:
    print("false")



  

