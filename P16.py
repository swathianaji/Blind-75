"""
Problem: 20. Valid Parentheses

URL: https://leetcode.com/problems/valid-parentheses/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# if len of stack below one, append value to stack

def isValid(s):
    stack = []
    for i in s:
        if len(stack) > 0:
            if (i ==')' and stack[-1] == '(') or (i =='}' and stack[-1] == '{') or (i ==']' and stack[-1] == '['):
                stack.pop()
                # print(stack)
            else:
                stack.append(i)
        else:
            stack.append(i)
            # print(stack)
        # print(stack)
    return len(stack) == 0    

# Sample test case
print(isValid("()[]{}"))