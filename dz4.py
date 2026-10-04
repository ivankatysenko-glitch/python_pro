result = []

def divider(a, b):
    if a < b:
        raise ValueError("a менше за b")

    if b > 100:
        raise IndexError("b більше за 100")

    return a / b


data = [
    (10, 2),
    (2, 5),
    ("123", 4),
    (18, 0),
    ([], 15),
    (8, 4)
]

for key, value in data:
    try:
        res = divider(key, value)
        result.append(res)

    except ValueError as e:
        print("ValueError:", e)

    except IndexError as e:
        print("IndexError:", e)

    except ZeroDivisionError as e:
        print("ZeroDivisionError:", e)

    except TypeError as e:
        print("TypeError:", e)

print("Результат:", result)
