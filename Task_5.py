def removeOuterParentheses(self, s: str) -> str:
    stack = []
    fin_answer = []
    counter = 0
    for i in s:
        stack.append(i)
        if i == '(':
            counter += 1
        elif i == ')':
            counter -= 1
        if counter == 0:
            fin_answer += stack[1:-1]
            stack = []

    return "".join(fin_answer)