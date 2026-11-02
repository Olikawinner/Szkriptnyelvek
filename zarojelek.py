def test(expr):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in expr:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
            
    return len(stack) == 0

# Tesztek
print(test("((5+3)*2+1)"))                    # True
print(test("{[(3+1)+2]+}"))                  # True
print(test("(3+{1-1)}"))                     # False
print(test("[1+1]+(2*2)-{3/3}"))               # True
print(test("(({[(((1)-2)+3)-3]/3}-3)"))        # False