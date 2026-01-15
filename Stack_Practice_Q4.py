
# Balanced Parenthesis
# Check whether the mathematical operation is balanced by parenthesis or not


def is_balanced(expression):
    stack = []
    # Dictionary to map opening and closing parentheses
    matching_parentheses = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in "([{":  # If it's an opening parenthesis, push it to the stack
            stack.append(char)
        elif char in ")]}":  # If it's a closing parenthesis
            # Check if the stack is empty or doesn't match
            if not stack or stack[-1] != matching_parentheses[char]:
                return False
            stack.pop()  # Pop the matching opening parenthesis

    # If the stack is empty, the parentheses are balanced
    return not stack

# Test the function
expression = input("Enter the mathematical operation: ")
if is_balanced(expression):
    print("The expression is balanced.")
else:
    print("The expression is not balanced.")

