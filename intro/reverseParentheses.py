def reverseParentheses(s):

    for i in range(len(s)):
        if s[i] == '(':
            start_idx = i
        elif s[i] == ')':
            end_idx = i
            return reverseParentheses(s[:start_idx] + s[start_idx + 1:end_idx][::-1] + s[end_idx + 1:])

    return s