def is_balanced(string):
    stack = []
    # Dictionary for matching pairs
    matching_parenthesis = {')': '(', '}': '{', ']': '['}

    for char in string:
        if char in '({[':  # Opening brackets
            stack.append(char)
        elif char in ')}]':  # Closing brackets
            if not stack or stack[-1] != matching_parenthesis[char]:
                return False
            stack.pop()  # Remove the matched opening bracket

    return len(stack) == 0  # True if stack is empty, False otherwise


# Example Usage
test_string = "()"
print(is_balanced(test_string))  # Output: True

 # Output: True
