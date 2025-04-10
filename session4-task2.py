def calculator(a, b, op):
    op = op.lower()
    match op:
        case 'add':
            return a+b
        case 'subtract':
            return a-b
        case 'multiply':
            return a*b
        case 'divide':
            if b==0:
                return "Can't divide by zero"
            return a/b
        case _:
            return "Invalid operator"