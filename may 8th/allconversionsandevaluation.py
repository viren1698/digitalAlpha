OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2}



def infix_to_postfix(formula):
    stack = []  # only pop when the coming op has priority
    output = ''
    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()  # pop '('
        else:
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    # leftover
    while stack: output += stack.pop()
    print(output)
    return output



def postfix_to_infix(formula):
    stack = []
    prev_op = None
    for ch in formula:
        if not ch in OPERATORS:
            stack.append(ch)
        else:
            b = stack.pop()
            a = stack.pop()
            if prev_op and len(a) > 1 and PRIORITY[ch] > PRIORITY[prev_op]:
                # if previous operator has lower priority
                # add '()' to the previous a
                expr = '(' + a + ')' + ch + b
            else:
                expr = a + ch + b
            stack.append(expr)
            prev_op = ch
    print(stack[-1])
    return stack[-1]


def infix_to_prefix(formula):
    op_stack = []
    exp_stack = []
    for ch in formula:
        if not ch in OPERATORS:
            exp_stack.append(ch)
        elif ch == '(':
            op_stack.append(ch)
        elif ch == ')':
            while op_stack[-1] != '(':
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append(op + b + a)
            op_stack.pop()  # pop '('
        else:
            while op_stack and op_stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[op_stack[-1]]:
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append(op + b + a)
            op_stack.append(ch)

    # leftover
    while op_stack:
        op = op_stack.pop()
        a = exp_stack.pop()
        b = exp_stack.pop()
        exp_stack.append(op + b + a)
    print(exp_stack[-1])
    return exp_stack[-1]



def prefix_to_infix(formula):
    stack = []
    prev_op = None
    for ch in reversed(formula):
        if not ch in OPERATORS:
            stack.append(ch)
        else:
            a = stack.pop()
            b = stack.pop()
            if prev_op and PRIORITY[prev_op] < PRIORITY[ch]:
                exp = '(' + a + ')' + ch + b
            else:
                exp = a + ch + b
            stack.append(exp)
            prev_op = ch
    print(stack[-1])
    return stack[-1]




def evaluate_postfix(formula):
    stack = []
    for ch in formula:
        if ch not in OPERATORS:
            stack.append(float(ch))
        else:
            b = stack.pop()
            a = stack.pop()
            c = {'+': a + b, '-': a - b, '*': a * b, '/': a / b}[ch]
            stack.append(c)
    print(stack[-1])
    return stack[-1]


def evaluate_infix(formula):
    return evaluate_postfix(infix_to_postfix(formula))




def evaluate_prefix(formula):
    exps = list(formula)
    while len(exps) > 1:
        for i in range(len(exps) - 2):
            if exps[i] in OPERATORS:
                if not exps[i + 1] in OPERATORS and not exps[i + 2] in OPERATORS:
                    op, a, b = exps[i:i + 3]
                    a, b = map(float, [a, b])
                    c = {'+': a + b, '-': a - b, '*': a * b, '/': a / b}[op]
                    exps = exps[:i] + [c] + exps[i + 3:]
                    break
        print(exps)
    return exps[-1]


evaluate_infix('(1+((2+3)*(4*5)))')
evaluate_postfix('231*+9-')
# evaluate_prefix('+-7*46+2')

infix_to_postfix('a+b*(c^d-e)^(f+g*h)-i')
infix_to_prefix("(a-b/c)*(a/k-l)")
