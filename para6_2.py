try:
    print("start code")
    print(10/0)
    print("no errer")
except NameError:
    print("We have an errer!")
except ZeroDivisionError:
    print("We have an ZeroDivision error!")


print("Code after capsule")