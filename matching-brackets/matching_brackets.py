from collections import deque


def is_paired(input_string):
    stack = deque()
    bracket_map = {")": "(", "}": "{", "]": "["}

    for char in input_string:
        if char in bracket_map.values():
            stack.append(char)
        if char in bracket_map:
            if not stack or stack.pop() != bracket_map[char]:
                return False

    return not stack
