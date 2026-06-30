from collections import deque


def is_paired(input_string):
    stack = deque()
    opening = ("[", "{", "(")
    closing = ("]", "}", ")")

    for char in input_string:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if stack and char == ")" and stack[-1] == "(":
                stack.pop()
            elif stack and char == "]" and stack[-1] == "[":
                stack.pop()
            elif stack and char == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False

    if not stack:
        return True
    return False
