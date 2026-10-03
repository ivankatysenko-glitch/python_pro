def checker(func):
    def checker(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as exc:
            print(f"We have problems {exc}")
        else:
            print(f"No prblems. Result - {result}")
    return checker

@checker
def calculate(expr):
    return eval(expr)


calc = checker(calculate)
calc("2+2")
