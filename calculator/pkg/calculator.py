def calculator(equation: str) -> float:
    tokens = equation.split()
    if not tokens:
        raise ValueError("Empty equation")
    return parse_expression(tokens)

def get_precedence(op: str) -> int:
    if op in ("+", "-"):
        return 1
    if op in ("*", "/"):
        return 2
    return 0

def apply_op(op: str, b: float, a: float) -> float:
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b
    return 0

def parse_expression(tokens: list[str]) -> float:
    values = []
    ops = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.replace('.', '', 1).isdigit():
            values.append(float(token))
        elif token in ("+", "-", "*", "/"):
            while ops and get_precedence(ops[-1]) >= get_precedence(token):
                values.append(apply_op(ops.pop(), values.pop(), values.pop()))
            ops.append(token)
        else:
            raise ValueError(f"Invalid token: {token}")
        i += 1

    while ops:
        values.append(apply_op(ops.pop(), values.pop(), values.pop()))

    if len(values) != 1:
        raise ValueError("Invalid expression evaluation")
    return values[0]