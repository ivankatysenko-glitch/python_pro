def safe_calculator(func):
    def wrapper(expression):
        try:
            return func(expression)
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except SyntaxError:
            print("Error: Invalid expression syntax.")
        except Exception as e:
            print(f"Error: Something went wrong ({e}).")

        return None

    return wrapper


def calculate(expression):
    return eval(expression)


calculate = safe_calculator(calculate)

# Проверка работы:
print(calculate("2 + 2"))  # Выведет: 4
print(calculate("10 / 0"))  # Выведет ошибку и None