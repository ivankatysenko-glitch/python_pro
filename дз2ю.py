def calculate(expression):

    expr = str(expression).strip()

    if "/ 0" in expr or "/0" in expr:
        print("Error: Division by zero is not allowed.")
        return None

    if "+" in expr:
        parts = expr.split("+")
        return float(parts[0]) + float(parts[1])

    elif "-" in expr:
        parts = expr.split("-")
        return float(parts[0]) - float(parts[1])

    return None


print(calculate("5 + 3"))
print(calculate("5 - 3"))